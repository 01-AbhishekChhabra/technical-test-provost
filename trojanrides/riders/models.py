from django.db import models
from uuid import uuid4

class Riders(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
