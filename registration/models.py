from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_lenth=40, blank=True)
    key_expires = models.DateTimeField()

    def __str__(self):
        return self.user

#    class Meta:
#        verbose_name_plural = u 'Perfiles de Usuario'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    objects = models.Manager()

 