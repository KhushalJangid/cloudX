from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

_branches = [("cse","Computer Science & Engineering"),
             ("it","Information Technology"),
             ("ai","Artificial Intelligence & Data Science"),
             ("csa","Computer Science & Engineering with AI"),
             ("ee","Electrical Engineering")
             ]

_posts = [("st","Student"),
          ("fc","Faculty"),
          ("ad","Admin")]

_genders = [("m","Male"),
           ("f","Female"),
           ("o","Others")]

_bg = [("a","A"),
       ("b","B"),
       ("o","O")]

_year = [
    (1,"First"),
    (2,"Second"),
    (3,"Third"),
    (4,"Fourth"),
]
class User(AbstractUser):
    username = None
    id=models.BigAutoField(primary_key=True)
    avatar = models.ImageField(upload_to='avatars/',default='avatars/profile-user.png')
    email = models.EmailField(unique=True)
    phone = models.CharField(blank=True,null=True,unique=True,max_length=15)
    # post = models.CharField(max_length=10,choices=_posts)

    objects = UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    # active = models.BooleanField(default=False)
    user_obj = models.OneToOneField(to = User,on_delete=models.CASCADE)
    rollno = models.CharField(null=True,unique=True,max_length=15)
    semester = models.IntegerField()
    f_name = models.CharField(blank=True,null=True,max_length=40)
    f_phone = models.CharField(blank=True,null=True,unique=True,max_length=15)
    m_name = models.CharField(blank=True,null=True,max_length=40)
    m_phone = models.CharField(blank=True,null=True,unique=True,max_length=15)
    gender = models.CharField(blank=True,null=True,max_length=10,choices=_genders)
    dob = models.DateField()
    address = models.TextField(blank=True,null=True,max_length=200)

