from django import forms
from .models import Tutorial


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ('tutorial_title','tutorial_content','img')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.label = ''
            visible.field.widget.attrs['placeholder'] = visible.name



