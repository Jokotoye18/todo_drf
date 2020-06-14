from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from  rest_auth.views import LoginView
from  rest_auth.serializers import LoginSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.exceptions import PermissionDenied

class TodoListView(ListCreateAPIView):
    serializer_class = TodoSerializer
    #get_todo_list by request.user
    def get_queryset(self):
        return Todo.objects.filter(added_by=self.request.user)

    #populate the added_by field during post request by request.user
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class TodoDetailView(RetrieveDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not view this todo')
        return super().get( request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not delete this todo')
        return super().delete(request, *args, **kwargs)

class TodoUpdateView(RetrieveUpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not view this todo')
        return super().get( request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not update this todo')
        return super().put( request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not update this todo')
        return super().patch( request, *args, **kwargs)