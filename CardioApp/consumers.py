from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import JsonWebsocketConsumer
import asyncio
import json


class PointerConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['id']
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
    
            
 