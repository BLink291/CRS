from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activate( models.Model ):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    secret_key = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
