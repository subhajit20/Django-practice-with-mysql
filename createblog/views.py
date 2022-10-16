from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .serializer import UserSerializer,LoginSerializer
from .models import User
from django.db import connection
from datetime import  datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(["GET","POST"])
def Signup(request):
    if request.method == 'POST':
        userdata = UserSerializer(data=request.data,context=request.data)
        if userdata.is_valid():
            today = datetime.today()
            username = userdata.data['username']
            email = userdata.data['email']
            password = userdata.data['password']
            encodedpassword = password.encode() 
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO createblog_user (username,email,password,account_creation_date) values (%s,%s,%s,'{creation_date}')".format(creation_date=str(today)),[username,email,encodedpassword])
                finally:
                    res = cursor.close()
            return Response({"success":{"msg":"Your have successfully created your account..."}})
        else:
            return Response({"error":userdata.errors})
    else:
        return Response({"msg":"This is signup route..."})

@api_view(["POST"])
def Login(request):
    if request.method == 'POST':
        loginSerializer = LoginSerializer(data=request.data,context=request.data)
        if loginSerializer.is_valid():
            username = loginSerializer.data.get("username")
            password = loginSerializer.data.get("password")
            myuser = User.objects.get(username=username)
            if myuser is not None:
                if myuser.password == password:
                    token = get_tokens_for_user(myuser)
                    return Response({'msg':token})
            return Response({'msg':'Username and password is not valid...'})
        return Response({'error':{'msg':loginSerializer.errors}})

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def HomePage(request):
    print(request)
    return Response({"msg":"This is home route"})