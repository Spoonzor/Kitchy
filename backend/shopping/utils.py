from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def send_shopping_notification(user_id, item_name):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {
            "type": "send_notification",
            "message": f"Nouvel article ajouté dans votre liste d'épicerie : {item_name}"
        }
    )
