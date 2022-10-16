from rest_framework import serializers
from .models import Student,Notes

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = ["email","password","stream"]

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields=["blog_info"]