from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    img = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    post_title = models.CharField(max_length=80, blank=False)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-created_at']
