from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.consumer import SyncConsumer, AsyncConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(SyncConsumer):

    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_.add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data = json.dumps({'status': 'First django channel connection has been established'}))

    def receive(self):
        print("receiver method")

    def disconnect(self):
        print("disconnected method")


class TestConsumera(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_.add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data = json.dumps({'status': 'First django channel connection has been established'}))

    async def receive(self):
        print("receiver method")

    async def disconnect(self):
        print("disconnected method")