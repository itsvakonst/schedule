from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    telegram_id = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    notify_by_email = models.BooleanField(default=True)
    notify_by_telegram = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False) 

    def __str__(self):
        return self.username

    


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} — {self.date}"


class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
