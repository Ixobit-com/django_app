from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
