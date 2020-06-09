from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    course_choices = (
        ('1', 'B.Tech'),
        ('2', 'MCA'),
        ('3', 'BCA'),

    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField('email', unique=True, blank=False)
    description = models.TextField(max_length=100, blank=True)
    course = models.CharField(choices=course_choices, max_length=2)
    # slug = models.SlugField(allow_unicode=True, unique=True)

    def get_absolute_url(self):
        return reverse('Users:user_profile', kwargs={'pk':self.pk})
