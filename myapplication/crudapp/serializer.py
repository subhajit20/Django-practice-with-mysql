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


   def validate_EmployeeName(self, value):
      if len(value) <= 3:
         raise serializers.ValidationError("Employeename is too sort")
      if len(value) >= 10:
         raise serializers.ValidationError("Employeename is too long")
      return value


   def validate_Department(self, value):
      if len(value) <= 3:
         raise serializers.ValidationError("Departmane name is too sort")
      if len(value) >= 10:
         raise serializers.ValidationError("Departmane is too long")
      return value