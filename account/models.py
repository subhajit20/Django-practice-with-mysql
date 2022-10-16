from ast import Delete
from tkinter import CASCADE
from django.db import connection
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import (
    make_password,
    check_password
)
from .MyUserManager import MyUserManager

# Create your models here.
class Student(AbstractBaseUser):
    id = models.AutoField(primary_key=True,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(("password"), max_length=128)
    firstname = models.CharField(max_length=200,default=False,editable=True,blank=True)
    lastname = models.CharField(max_length=200,default=False,editable=True,blank=True)
    stream = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = MyUserManager()


    @classmethod
    def CreateStudent(cls,email,password,stream):
        hasedpassword = make_password(password)
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO account_student (email,password,stream,firstname,lastname) VALUES (%s,%s,%s,%s,%s);',[email,hasedpassword,stream,'',''])
        return True

    @classmethod
    def GetStudent(cls,email,password):
        get_student = cls.objects.get(email=email)
        dcrypted_password = check_password(password,get_student.password)
        # print(dcrypted_password)
        if get_student and dcrypted_password:
            return {'flag':True,'std':get_student}
        else:
            return {'flag':False,'std':'No students are there'}

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Notes(models.Model):
    blog_id = models.AutoField(primary_key=True,unique=True)
    blog_info = models.CharField(max_length=400,blank=False,editable=True)
    blog_upload_date = models.DateTimeField(auto_now_add=True)
    blog_writer = models.ManyToManyField(Student)

    def __str__(self):
        return self.blog_info

    @classmethod
    def Create_Blog(cls,blogname,user):
        std = cls.objects.create(blog_info=blogname)
        std.blog_writer.add(user)
        std.save()
        return True
    
    @classmethod
    def Get_Notes(cls,user):
        notes = list(cls.objects.all().filter(blog_writer=user).values())
        return notes