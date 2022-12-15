import uuid
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    db_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    movie_id = models.CharField(max_length=10)
    def __str__(self):
        return self.movie_id
