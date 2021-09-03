from django.contrib.auth.models import AbstractUser
from django.db import models

class UserNet(AbstractUser):
    '''Custom model user'''

    GENDER = (
        ('male', 'male'),
        ('female', 'female'),

    )
    midle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, default='male')
    user_permissions = []
    groups = []
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name