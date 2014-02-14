from django.conf.urls import patterns, include, url
from core.views import Index, TodoListAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoListAPI)

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='core.index'),
    url(r'^api/', include(router.urls)),
)
