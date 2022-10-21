from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from json import dumps
from channels.layers import get_channel_layer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "CSE"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.channel_name
        )
        self.accept()
        msg = {'msg':f'{self.channel_name} has joined the {self.room_name} group ...'}

        # self.channel_layer.group_send = It sends the "New user joined message" message to all the recipents of the group currently joined,
        # But the thing is group_send method only send the message the to the specific group which we have declared at below , but now we need to send the message to our front end so that we can access the message which server has sent to the group , That's why group_send takes two parameter where we need to specify a function name which takes the message all the way from server to client ...
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,{
                "type":"join_message", # <---------- join_message this is a funtion which will be made by us 
                "message":msg
            }
        )
    
    def join_message(self,event): #  <----- This is the function which takes the joinning message to our client 
        message = event["message"]
        group = get_channel_layer() # with the help of get_channel_layer() funtion --> we can call our group with its name and can send messages to it from any other functions from any other different apps
        # Send message to WebSocket. Not only from consumer , we can also call this function from anywhere in our project
        self.send(text_data=dumps(message))


    def send_notification(self,event):
        message = event["message"]

        self.send(text_data=dumps(message))


    def user_joined(self,event):
        message = event["message"]

        self.send(text_data=dumps(message))
        
    def receive(self, text_data=None, bytes_data=None):
        print("From receiver --> ",text_data)
        self.send(text_data=text_data)

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )
        self.close()


