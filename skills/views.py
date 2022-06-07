from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill


def index(request):
    skill = Skill.objects.all()
    context = {'skills': skill,
               'name_skill': 'Список навыков'}
    return render(request, 'skills/index.html', context=context)
