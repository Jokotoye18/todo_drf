from django.test import TestCase
from todo.models import Todo
from django.contrib.auth import get_user_model


class TodoViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_user2',
            email = 'test2@gmail.com'
        )

        self.todo = Todo.objects.create(
            title = 'Test todo',
            added_by = self.user
        )

