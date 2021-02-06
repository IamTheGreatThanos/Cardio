from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import JsonWebsocketConsumer
import asyncio
import json
import urllib.parse

class PointerConsumer(JsonWebsocketConsumer):
    def connect(self):
        # self.group_name = "room_"+str(self.scope['wid'])
        # self.group_name = "room_"+str(self.scope["url_route"]["kwargs"]["wid"])
        params = urllib.parse.parse_qs(self.scope['query_string'].decode('utf8'))
        self.group_name = "user"
        print(params)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()    

    def disconnect(self, code):
        if hasattr(self, 'group_name'):
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name
            )
    
    def send_point(self, event):
        self.send_json({
            'content': {
                'pointers': event
            }
        })
    
            
 