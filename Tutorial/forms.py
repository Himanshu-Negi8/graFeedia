from django import forms
from .models import Tutorial


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ('tutorial_title','tutorial_content')



