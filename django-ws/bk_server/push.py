import time

import channels.layers
from asgiref.sync import async_to_sync


channel_layer = channels.layers.get_channel_layer()

while True:
    async_to_sync(channel_layer.group_send)(
        'push_test', 
        {'type': 'chat_message','message': time.time()}
    )
    time.sleep(3)
