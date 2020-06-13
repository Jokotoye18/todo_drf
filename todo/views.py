from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from  rest_auth.views import LoginView
from  rest_auth.serializers import LoginSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView

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

class TodoUpdateView(RetrieveUpdateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()