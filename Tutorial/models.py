from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

from django.urls import reverse
from django.utils.text import slugify
User = get_user_model()


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    # user = models.ForeignKey(User,related_name='tutorial',on_delete=models.CASCADE)
    tutorial_category = models.ForeignKey(TutorialCategory,default=1,verbose_name='Category',
                                          on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    series_slug = models.CharField(max_length=200)
    img = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    user = models.ForeignKey(User,related_name='tutorial',on_delete=models.CASCADE)
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now())
    tutorial_series =models.ForeignKey(TutorialSeries,on_delete=models.CASCADE)
    tutorial_slug = models.SlugField(allow_unicode=True,unique=True)
    img = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)

    def save(self, *args, **kwargs):
        self.tutorial_slug = slugify(self.tutorial_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tutorial_title

    def get_absolute_url(self):
        return reverse('Tutorial:tutorial_detail', kwargs={'slug': self.tutorial_slug})


class Moments(models.Model):

    title = models.CharField(max_length=200)
    pic=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
