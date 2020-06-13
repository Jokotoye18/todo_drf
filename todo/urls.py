from django.urls import path
from .views import (
    TodoListView, 
    TodoDetailView,
    TodoUpdateView
)


urlpatterns = [
    path('', TodoListView.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
]
