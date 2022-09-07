from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudapp.models import Employee
from crudapp.serializer import EmployeeSerializer

# Create your views here.
@api_view(['GET'])
def get_homepage(request):
    return Response({'msg':'This is my crud app...'})

@api_view(['POST'])
def insert_employee(request):
    if request.method == 'POST':
        employess = Employee.objects.raw('SELECT * FROM crudapp_employee WHERE EmployeeId = "1"')
        if employess == None:
            return Response({'msg':'No employees tables are there...'})
        else:
            emps = EmployeeSerializer(employess,many=True)
            print(emps.data)
            return Response({'msg':emps.data})