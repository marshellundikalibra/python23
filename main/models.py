from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Post(models.Model):
    author=models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    body=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)

# class User(models.Model):
    def __str__(self):
        return f"{self.author.username} -> {self.body}"






