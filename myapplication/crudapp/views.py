from random import random
from sqlite3 import Date
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudapp import serializer
from crudapp.models import Employee
from crudapp.serializer import EmployeeSerializer,SearchEmployee
from django.db import connection


# Create your views here.
@api_view(['GET'])
def get_homepage(request):
    return Response({'msg':'This is my crud app...'})

@api_view(['GET'])
def get_AllEmployee(request):
        employess = Employee.objects.raw('SELECT * FROM crudapp_employee ')
        if employess == None:
            return Response({'msg':'No employees tables are there...'})
        else:
            emps = EmployeeSerializer(employess,many=True)
            if len(emps.data) > 0:
                return Response({'msg':emps.data})
            else:
                return Response({'msg':'No employees tables are there...'})

@api_view(['POST'])
def insert_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            emp_name = serializer.initial_data["EmployeeName"]
            department = serializer.initial_data["Department"]
            date = Date.today()
            with connection.cursor() as cursor:
                id = int(random()*10000000)
                print(id)
                cursor.execute("INSERT INTO crudapp_employee values ({m},%s,%s,%s)".format(m=id),[emp_name,department,date])
            return Response({'msg':'Employee has successfully been added...'})
        else:
            return Response({'msg':serializer.errors})


@api_view(['POST'])
def delete_employee(request):
    if request.method == 'POST':
        data1 = EmployeeSerializer(data=request.data)
        emp_name = data1.initial_data["EmployeeName"]
        with connection.cursor() as cursor: 
            cursor.execute("DELETE FROM crudapp_employee where EmployeeName = '{emp}'".format(emp=emp_name))
            if cursor:
                rs = 'Deleted Employee'
            else:
                rs = 'Not Deleted'
        return Response({'msg':rs})

@api_view(['POST'])
def validation_middleware(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            return Response({'mdg':"Data is okk"})
        else:
            print(serializer.data["EmployeeName"])
            return Response({'msg':[serializer.errors]})

@api_view(['POST'])
def search_employee(request):
    if request.method == 'POST':
        serializer = SearchEmployee(data=request.data)
        if serializer.is_valid():
            req = serializer.data['EmployeeName']
            # print(req)
            empl = Employee.objects.raw('SELECT EmployeeName,Department FROM crudapp_employee WHERE EmployeeName = "{d}"'.format(d=req))
            with connection.cursor() as cursor: 
                cursor.execute('SELECT EmployeeName,Department FROM crudapp_employee WHERE EmployeeName = "{s}"'.format(s=req))
                row = cursor.fetchone()
            if row == None:
                return Response({'msg':"No employes are there with this name"})
            return Response({'msg':row})
        return Response({'msg':serializer.errors})