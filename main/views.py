# from contextlib import redirect_stdout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required,permission_required
# from Accounts.tests import send_otp
from main.models import Data
from pandas import DataFrame as df
# Create your views here.
from pathlib import Path
from os import path,remove
from cloudX.settings import MEDIA_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(path.abspath(__file__)).parent.parent
BASE_URL = "http://127.0.0.1:8000/"

def parseGet(request,kw):
    if request.GET.get(kw):
        return request.GET.get(kw)
    else:
        return ""

@login_required
@permission_required("isSuperuser",raise_exception=True)
def download(request):
    _from = parseGet(request,"from")
    _to = parseGet(request,"to")
    _type = parseGet(request,"type")
    print(_from,_to,_type)
    if _type != "all":
        query = Data.objects.filter(type__icontains=_type)
    else :
        query = Data.objects.all()
    if _to != "":
        query = query.filter(date__lte = _to)
    if _from != "":
        query = query.filter(date__gte = _from)
    filename = parse_data(query)
    if filename == None:
        return redirect("/")
    filepath = path.join(BASE_DIR,filename)
    if path.exists(filepath):
        with open(filepath, "rb") as excel:
            data = excel.read()
        response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=data.xlsx'
        return response

@login_required
def filter(request):
    _from = parseGet(request,"from")
    _to = parseGet(request,"to")
    _type = parseGet(request,"type")
    print(_from,_to,_type)
    if _type != "all":
        query = Data.objects.filter(type__icontains=_type)
    else :
        query = Data.objects.all()
    if _to != "":
        query = query.filter(date__lte = _to)
    if _from != "":
        query = query.filter(date__gte = _from)
    if request.user.is_superuser:
        user = request.user
        data = {}
        i=1
        for k in query:
            data[i] = {
                "id":k.id,
                "title":k.title,
                "type":k.get_type_display(),
                "uname": f"{k.user.first_name} {k.user.last_name}",
                "date":k.date
            }
            i+=1
        ctx = {
            "avatar": user.avatar,
            "name":f"{user.first_name} {user.last_name}",
            "data":data,
        }
        return render(request,"dashboard_teacher.html",ctx)
    else:
        user = request.user
        data = {}
        i=1
        for k in query:
            data[i] = {
                "id":k.id,
                "title":k.title,
                "type":k.get_type_display(),
                "date":k.date
            }
            i+=1
        ctx = {
            "avatar": user.avatar,
            "name":f"{user.first_name} {user.last_name}",
            "data":data,
        }
        return render(request,"dashboard_student.html",ctx)
        
        
@login_required
def home(request):
    if request.user.is_superuser:
        user = request.user
        query = Data.objects.all()[0:20]
        data = {}
        i=1
        for k in query:
            data[i] = {
                "id":k.id,
                "title":k.title,
                "type":k.get_type_display(),
                "uname": f"{k.user.first_name} {k.user.last_name}",
                "uid": k.user.id,
                "date":k.date
            }
            i+=1
        ctx = {
            "avatar": user.avatar,
            "name":f"{user.first_name} {user.last_name}",
            "data":data,
        }
        return render(request,"dashboard_teacher.html",ctx)
    else:
        user = request.user
        query = Data.objects.filter(user=request.user)
        data = {}
        i=1
        for k in query:
            data[i] = {
                "id":k.id,
                "title":k.title,
                "type":k.get_type_display(),
                "date":k.date
            }
            i+=1
        ctx = {
            "avatar": user.avatar,
            "name":f"{user.first_name} {user.last_name}",
            "data":data,
        }
        return render(request,"dashboard_student.html",ctx)


@login_required
def upload(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        link = request.POST.get('verification-link')
        type = request.POST.get('type')
        date = request.POST.get('date')
        file = request.FILES.get('file')
        Data.objects.create(
            title=title,
            user = request.user,
            description=description,
            type=type,
            date=date,
            link=link,
            file=file,
        )
        return redirect("/")
    return render(request,'upload_form.html')

@login_required
def edit(request,id):
    if request.method == "POST":
        query = Data.objects.get(id=id)
        if query.user == request.user:
            title = request.POST.get('title')
            description = request.POST.get('description')
            link = request.POST.get('verification-link')
            type = request.POST.get('type')
            date = request.POST.get('date')
            file = request.FILES.get('file')
            query.title=title
            query.description=description
            query.type=type
            query.date=date
            query.link=link
            if file != None:
                remove(path.join(MEDIA_ROOT,query.file.name))
                query.file=file
            query.save()
            return redirect("/")
        else:
            return Response("You are not Authorized",status=status.HTTP_403_FORBIDDEN)
    query = Data.objects.get(id=id)
    print(query.file)
    ext = query.extension()
    ctx = {
        "title":query.title,
        "description":query.description,
        "type":query.type,
        "date":query.date.strftime("%Y-%m-%d"),
        "link":query.link,
        "file":query.file,
        "filetype": "pdf" if ext == ".pdf" else "image"
    }
    return render(request,'edit_doc.html',ctx)
    
    
@login_required
def view(request,id):
    query = Data.objects.get(id=id)
    ext = query.extension()
    ctx = {
        "title":query.title,
        "description":query.description,
        "type":query.get_type_display(),
        "date":query.date,
        "link":query.link,
        "file":query.file,
        "filetype": "pdf" if ext == ".pdf" else "image"
        
    }
    return render(request,'view_doc.html',ctx)
 
@login_required
def delete(request,id):
    query = Data.objects.get(id=id)
    if request.user == query.user:
        query.delete()
        return redirect("/")
    else :
        return HttpResponse("You are not authorized")
    
    
def parse_data(queryset):
    filename = "data.xlsx"
    # data = list(Data.objects.all().values())
    data = list(queryset.values())
    if data == []:
        return None
    data = df(data)
    # data.set_index("id")
    data.loc[:,"file"] = [ f"{BASE_URL}media/{x}" for x in data.loc[:,"file"]]
    data.to_excel(filename,index=False)
    return filename
    
    