from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('skill/<int:skill_id>/', view_skills, name='view_skills'),
]