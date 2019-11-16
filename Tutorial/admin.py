from django.contrib import admin
from .models import TutorialCategory,TutorialSeries,Tutorial
# Register your models here.
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial)