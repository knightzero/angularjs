from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from rest_framework.renderers import JSONRenderer
import redis
from ws4redis import settings as redis_settings

redisConnection = redis.StrictRedis(**redis_settings.WS4REDIS_CONNECTION)

@receiver(post_save)
def websocksCreat(sender, instance, **kwargs):
    data = {}
    data['status'] = 'updated'
    redisConnection.publish('_broadcast_:', JSONRenderer().render(data))
    
@receiver(post_delete)
def websocksDelete(sender, instance, **kwargs):
    data = {}
    data['status'] = 'updated'
    redisConnection.publish('_broadcast_:', JSONRenderer().render(data))
    