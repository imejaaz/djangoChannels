from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.consumer import SyncConsumer, AsyncConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(SyncConsumer):
    def websocket_connect(self, event):

        self.send({
            "type": "websocket.accept",
        })
        print("connected...")

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": json.dumps({
                "message": event["text"],
            }),
        })
        print('receiving data it now..............', event)

    def websocket_disconnect(self, event):
        print("about to diconnect now")



class TestConsumera(AsyncConsumer):

    def connect(self, event):
        print("connected ..........cc", event)
        

    def receive(self, event):
        print("receiver method", event)

    def disconnect(self, event):
        print("disconnected method.............", event)



        print("disconnected method")