from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill


def index(request):
    skill = Skill.objects.order_by('-created_at')
    return render(request, 'skills/index.html', context={'skills': skill, 'name_skill': 'Список навыков'})

