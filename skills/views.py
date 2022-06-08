from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, Category


def index(request):
    skill = Skill.objects.all()
    categories = Category.objects.all()
    context = {'skills': skill,
               'name_skill': 'Список навыков',
               'categories': categories,}
    return render(request, 'skills/index.html', context=context)


def get_category(request, category_id):
    skills = Skill.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='skills/category.html', context={
        'skills': skills,
        'categories': categories,
        'category': category
    })