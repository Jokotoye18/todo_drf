from django.test import TestCase
from todo.models import Todo
from django.contrib.auth import get_user_model


class TodoModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test_user',
            email = 'test@gmail.com'
        )

        self.todo = Todo.objects.create(
            title = 'Test todo',
            added_by = self.user
        )

    def test_todo_model_content(self):
        todo = Todo.objects.get(pk=1)
        todos = Todo.objects.count()
        self.assertEqual(todos, 1)
        self.assertEqual(f'{todo.title}', 'Test todo')
        self.assertEqual(todo.added_by, self.user)
    
    def test_todo_model_text_representation(self):
        todo = Todo.objects.get(pk=1)
        response = f'{todo}'
        self.assertEqual(response, 'Test todo')


