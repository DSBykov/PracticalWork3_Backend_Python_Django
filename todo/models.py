
from django.db import models
from django.db.models import CharField, TextField, BooleanField, DateTimeField


# Create your models here.

class Task(models.Model):
    title = CharField(max_length=128)
    description = TextField(max_length=512)
    completed = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)