from django.urls import path
from .views import (
    TodoListView, 
    TodoDetailView,
    ApiRoot
    # TodoUpdateView,
)


urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
    path('todos', TodoListView.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    # path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
]
