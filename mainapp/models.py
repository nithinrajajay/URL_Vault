from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Date = models.DateTimeField(default=timezone.now)
    URL = models.URLField(max_length=200)
