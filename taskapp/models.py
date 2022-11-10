from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title


    @property
    def preview(self):
        return self.description[:50]

    class Meta:
        ordering = ['-updated_at','-created_at']