from django.shortcuts import render
from rest_framework import viewsets,serializers
from .models import Todo

# Create your views here.


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'processing', 'completed','staff')

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
