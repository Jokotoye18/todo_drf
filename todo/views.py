from django.shortcuts import render, redirect, get_object_or_404
from .serializer import TodoSerializer
from .models import Todo
from  rest_auth.views import LoginView
from  rest_auth.serializers import LoginSerializer
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework.filters import OrderingFilter
from rest_auth import urls
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)


class ApiRoot(APIView):
    permission_classes = [AllowAny,]
    def get(self, request, *args, **kwargs):
        data = {
            'todo_list': reverse('todos', request=request),
            'sign up': reverse('rest_register', request=request),
            'read docs': reverse('schema-redoc', request=request),
        }
        return Response(data)


class TodoListView(ListCreateAPIView):
    serializer_class = TodoSerializer
    # queryset = Todo.objects.all()

    #get_todo_list by request.user
    def get_queryset(self):
        todos = Todo.objects.filter(added_by=self.request.user)
        return todos.order_by('-timestamp')

    #populate the added_by field during post request with request.user
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not view this todo')
        return super().get( request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo ,pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not update this todo')
        return super().put( request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo ,pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not update this todo')
        return super().patch( request, *args, **kwargs)  

    def delete(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=self.kwargs.get('pk'))
        if todo.added_by != request.user:
            raise PermissionDenied('You can not delete this todo')
        return super().delete(request, *args, **kwargs)

# class TodoUpdateView(RetrieveUpdateAPIView):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()

#     def get(self, request, *args, **kwargs):
#         todo = get_object_or_404(Todo ,pk=self.kwargs.get('pk'))
#         if todo.added_by != request.user:
#             raise PermissionDenied('You can not view this todo')
#         return super().get( request, *args, **kwargs)

    
