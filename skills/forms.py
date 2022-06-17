from django import forms
from .models import Category
from .models import Skill

# Форма не связанная с моделью
# class SkillsForm(forms.Form):
#     name_skill = forms.CharField(
#         max_length=50,
#         label='Названые навыка',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         ))
#     description = forms.CharField(
#         label='Описание навыка',
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'rows': 5,
#             }
#         ))
#
#
#     is_published = forms.BooleanField(
#         label='Навык освоен?',
#         initial=True
#     )
#
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         label='Категория',
#         empty_label='Выберите категорию',
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )


# Форма связанная с моделью
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skill
        #fields = '__all__'
        fields = ['name_skill', 'description', 'is_published', 'category']
        widgets = {
            'name_skill': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }