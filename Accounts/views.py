# from json import loads
# from .tests import send_otp
# from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Student, User
from django.contrib.auth.decorators import login_required,permission_required
from Accounts.serializers import studentSerializer
# Create your views here.

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request,user)
            user = User.objects.get(email=email)
            if not user.is_superuser:
                try :
                    student = Student.objects.get(user_obj=user)
                except Exception as e:
                    print(e)
                    return redirect("/accounts/profile")
            route = request.GET.get("next")
            if route:
                return redirect(route)
            return redirect("/")
        else:
            return HttpResponse(content="Invalid credentials",status=403)
        
    return render(request,"accounts/login_form.html")


@login_required
@permission_required("isSuperuser",raise_exception=True)
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password0 = request.POST.get("password-0")
        name = name.split()
        if email.split("@")[-1] != "jecrc.ac.in":
            # messages.error(request, 'Invalid email.')
            # return redirect("/accounts/add_student")
            return HttpResponse("Invalid Email")
        if password == password0:
            print("here")
            try :
                user = User.objects.create_user(first_name=name[0], last_name=name[-1],
                                            email=email, password=password)
                return redirect("/")
            except Exception as e:
                print(e)
                user = User.objects.get(email=email)
                if user.is_active:
                    # messages.error(request, 'User Already Exists.')
                    # return redirect("/accounts/add_student")
                    return HttpResponse("User Already Exists")
    return render(request,"accounts/add_student.html")


@login_required
@permission_required("isSuperuser",raise_exception=True)
def add_faculty(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password0 = request.POST.get("password-0")
        name = name.split()
        if email.split("@")[-1] != "jecrc.ac.in":
            messages.error(request, 'Invalid email.')
            return redirect("/accounts/add_faculty")
        if password == password0:
            try :
                user = User.objects.create_user(first_name=name[0], last_name=name[-1],
                                            email=email, password=password,superuser=True)
                return redirect("/")
            except Exception as e:
                print(e)
                user = User.objects.get(email=email)
                if user.is_active:
                    messages.error(request, 'User Already Exists.')
                    return redirect("/accounts/add_faculty")
    return render(request,"accounts/add_faculty.html")

  
@login_required
def logoutUser(request):
    logout(request)
    return redirect("/")    
    
@login_required
def profile(request):
    if request.method == "POST":
        phone = request.POST.get("student-phoneNumber")
        rollno = request.POST.get("rollno")
        sem = int(request.POST.get("semester"))
        f_name = request.POST.get("father-name")
        m_name = request.POST.get("mother-name")
        f_phone = request.POST.get("father-phone-number")
        m_phone = request.POST.get("mother-phone-number")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        user = request.user
        try :
            st = Student.objects.get(user_obj=user)
            print(dob)
            user.phone = phone
            user.save()
            st.rollno=rollno
            st.semester = sem
            st.f_name = f_name
            st.f_phone = f_phone
            st.m_name = m_name
            st.m_phone = m_phone
            st.gender = gender
            st.dob=dob
            st.address = address 
            st.save()
            return redirect("/")
        except Student.DoesNotExist:
            user.phone = phone
            user.save()
            Student.objects.create(
                user_obj=user,
                rollno=rollno,
                semester = sem,
                f_name = f_name,
                f_phone = f_phone,
                m_name = m_name,
                m_phone = m_phone,
                gender = gender,
                dob=dob,
                address = address 
            )
            return redirect("/")
    user = request.user
    try:
        meta = studentSerializer(Student.objects.get(user_obj=user))
    except:
        meta = {}
    context = {"user":user,"meta":meta}
    return render(request,"accounts/edit_profile.html",context)

@login_required
@permission_required("isSuperuser",raise_exception=True)
def view_profile(request,id):
    user = User.objects.get(id=id)
    try:
        meta = studentSerializer(Student.objects.get(user_obj=user))
    except:
        meta = {}
    context = {"user":user,"meta":meta}
    return render(request,"accounts/view_profile.html",context)
