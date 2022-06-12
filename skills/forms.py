from django import forms
from .models import Category


class SkillsForm(forms.Form):
    name_skill = forms.CharField(max_length=50)
    description = forms.CharField()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())