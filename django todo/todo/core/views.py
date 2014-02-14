from django.views.generic import TemplateView
from core.models import Todo
from rest_framework import viewsets
from core.serializers import TodoSerializer

class Index(TemplateView):
    template_name = "index.html"

class TodoListAPI(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class  = TodoSerializer