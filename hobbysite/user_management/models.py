from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63)
    email_address = models.EmailField()

    def __str__(self):
        return self.user.username