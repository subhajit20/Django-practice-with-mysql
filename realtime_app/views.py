from cgitb import text
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TextSerializer,ChannelUser
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.

@api_view(['GET','POST'])
def Home(request):
    data = request.data
    serializer = TextSerializer(data=data)
    if serializer.is_valid():
        layer = get_channel_layer()
        text_data = serializer.data.get('text')
        async_to_sync(layer.group_send)(
            "CSE",{
                "type":"send_notification",
                "message":text_data
            }
        )
        return Response({'msg':"Hellow this is realtime app route..."})
    return Response({'msg':serializer.errors})
