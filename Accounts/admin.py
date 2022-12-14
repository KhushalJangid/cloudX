# from cProfile import label
from django.contrib import admin
from .models import User, Student
from .forms import UserChangeForm, UserCreationForm
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    # form = UserChangeForm
    add_form = UserCreationForm
    # add_form = UserCreateForm
    list_display = ["email","phone","date_joined"]
    search_fields = ["email","first_name","phone"]
    readonly_fields = ["date_joined","last_login"]
    
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': (
    #             # 'first_name' , 
    #             #   'last_name', 
    #               'username',
    #             #   'rollno',
    #             #   'email',
    #             #   'phone',
    #             #   'avatar',
    #             #   'address',
    #               'password' ),
    #     }),
    # )
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering =()

admin.site.register(User,AccountAdmin)
admin.site.register(Student)