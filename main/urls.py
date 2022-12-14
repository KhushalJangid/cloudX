from django.urls import path
from main import views

urlpatterns = [
    path("",views.home,name="home"),
    path("download",views.download),
    path("filter",views.filter),
    path('upload',views.upload),
    path('view/<int:id>',views.view),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete),
]