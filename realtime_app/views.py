from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def Home(self):
    return Response({'msg':"Hellow this is realtime app route..."})