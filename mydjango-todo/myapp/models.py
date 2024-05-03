from django.db import models


# class Item(models.Model):
#     name = models.CharField(max_length=30)
#     note = models.TextField()

class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    updated = models.DateTimeField()
    completed = models.BooleanField(default=False)

    