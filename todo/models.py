from django.db import models
from django.contrib.auth import get_user_model

class Todo(models.Model):
    title = models.CharField(max_length=150, help_text='150 char max')
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), related_name='todos', on_delete=models.CASCADE)

    objects = models.Manager

    def __str__(self):
        return self.title
