import re

from django.db import connection
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def validate_username(self,value):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * from createblog_user where username=%s',[value])
            row = cursor.fetchone()
        if row is not None:
            raise serializers.ValidationError("Username is already exist...Try with another valid username")
        elif len(value) <= 3:
            raise serializers.ValidationError("Username is too short...")
        elif len(value) >= 30:
            raise serializers.ValidationError("Username is too long...")
        else:
            return value

    def validate_email(self,value):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * from createblog_user where email=%s',[value])
            row = cursor.fetchone()
        if row is not None:
            raise serializers.ValidationError("Email is already exist...Try with another valid email")
        else:
            return value
    
    def validate_password(self,value):
        confirm_password = self.context["confirmpassword"]
        print(confirm_password)
        if len(value) < 8:
            raise serializers.ValidationError("Your Password should be 8 characters long...")
        elif re.search('[a-z]{2}[A-Z]{2}[0-9]{2}[!@#$%^&*]{2}',value) is None:
            raise serializers.ValidationError("Password must be at least 8 characters long & should contain at least 2 lowercase, 2 uppercase, 2 number & 2 symbol")
        elif value != confirm_password:
            raise serializers.ValidationError("Passwords are not matched...")
        else:
            return value

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    
    def validate_username(self,value):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * from createblog_user where username=%s',[value])
            row = cursor.fetchone()
        if row is not None:
            return value
        else:
            raise serializers.ValidationError("Username is not valid")
    
    def validate_password(self,value):
        myusername = self.context["username"]
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM createblog_user WHERE username="{userusername}" AND password=%s'.format(userusername=str(myusername)),[str(value)])
            row = cursor.fetchone()
        
        if row is not None:
            return value
        else:
            raise serializers.ValidationError("Username and Password is invalid")