from rest_framework import serializers
from crudapp.models import Department,Employee

class DepartmentSerializer(serializers.ModelSerializer):
   class meta:
        model = Department
        fields = ('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
   class Meta:
        model = Employee
        fields = ('EmployeeName','Department')
