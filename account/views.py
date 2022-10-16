from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .serializer import StudentSerializer,LoginSerializer,BlogSerializer
from .models import Student,Notes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(["POST"])
def CreateAccount(request):
    if request.method == 'POST':
        print(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            stream = serializer.data.get("stream")
            create = Student.CreateStudent(email,password,stream)
            print(request.user)
            return Response({'msg':serializer.data})
        return Response({'msg':serializer.errors})

@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            flag = Student.GetStudent(email,password)
            if flag['flag']:
                data = get_tokens_for_user(flag['std'])
                return Response({'msg':data})
            else:
                return Response({'msg':"You don't have any account with this email"})
        return Response({'msg':serializer.errors})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def HomePage(request):
    print(request.user)
    return Response({'msg':"Yppuu"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def CreateNote(request):
    if request.user is not None:
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog_info = serializer.data.get('blog_info')
            user = Student.objects.get(email=request.user)
            # print(user.id)
            flag = Notes.Create_Blog(blog_info,user)
            return Response({'msg':serializer.data.get('blog_info')})
        return Response({'msg':serializer.errors})
    return Response({'msg':"Yppuu"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def IAM(request):
    if request.user is not None:
        user = Student.objects.get(email=request.user)
        notes = Notes.Get_Notes(user)
        return Response({'msg':notes})
    return Response({'msg':"Yppuu"})