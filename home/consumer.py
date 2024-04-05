from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.consumer import SyncConsumer
import json
import asyncio


class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        # Explicitly accept the WebSocket connection
        await self.accept()
        print("Connected...")

        # Start the loop to send messages
        await self.send_messages_loop()

    async def send_messages_loop(self):
        for i in range(8):
            ++i
            await asyncio.sleep(1)  # Adjust the delay as needed
            await self.send(text_data=json.dumps({
                "text":str(i),
            }))

    async def websocket_receive(self, event):
        print('Receiving data now:', event)
        await self.send(text_data=json.dumps({
                "type": "websocket.send",
                "text": "Message from the server.",
            }))

    async def websocket_disconnect(self, event):
        print("About to disconnect now")



        
class MySyncConsumer(WebsocketConsumer):

    def websocket_connect(self, event):
        self.accept()
        self.send(text_data=json.dumps({
            "message": "Connection accepted.",
        }))
        print("Connected...")

    def websocket_receive(self, event):
        for i in range (5):
            self.send(text_data=json.dumps({
            "message": event["text"],
            }))
        print('Receiving data now:', event)

    def websocket_disconnect(self, event):
   
        print("About to disconnect now")







# from channels.consumer import SyncConsumer

# class MySyncConsumer(SyncConsumer):

#     def websocket_connect(self, event):

#         self.send({
#             "type": "websocket.accept",
#         })

#     def websocket_receive(self, event):
#         self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })
    
#     def websocket_disconnect(self, event):
#         self.send({'type':'Diconnected'})
#         print('diconnected...')