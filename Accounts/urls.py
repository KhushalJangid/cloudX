from django.urls import path
from django.urls import re_path
from Accounts import views

urlpatterns = [
    re_path(r'login/?$', views.login_user),
    re_path(r'logout/?$', views.logout),
    re_path(r'add_faculty/?$', views.add_faculty),
    re_path(r'add_student/?$', views.add_student),
    path('profile', views.profile),
    path('viewProfile/<int:id>', views.view_profile),
]
