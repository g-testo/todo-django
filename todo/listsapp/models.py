from django.db import models
from django.utils import timezone

class List(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=35)
    due_date = models.DateTimeField("due date")
    is_complete = models.BooleanField()
    todo_list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def is_past_due_date(self):
        return self.due_date <= timezone.now()