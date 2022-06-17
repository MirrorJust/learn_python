from django.shortcuts import render, get_object_or_404, redirect
from .models import Skill, Category
from .forms import SkillsForm


def index(request):
    skill = Skill.objects.all()
    context = {'skills': skill,
               'name_skill': 'Список навыков',
               }
    return render(request, 'skills/index.html', context=context)


def get_category(request, category_id):
    skills = Skill.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='skills/category.html', context={
        'skills': skills,
        'category': category
    })


def view_skills(request, skill_id):
    #skill_item = Skill.objects.get(pk=skill_id)
    skill_item = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'skills/view_skills.html', {'skill_item': skill_item})


def add_skill(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            #skill = Skill.objects.create(**form.cleaned_data)
            skill = form.save()
            return redirect(skill)
    else:
        form = SkillsForm()
    return render(request, 'skills/add_skill.html', {'form': form})
