from django.contrib import admin
from .models import Skill, Category


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_skill', 'created_at', 'update_at', 'category', 'is_published')
    list_display_links = ('id', 'name_skill')
    search_fields = ('name_skill', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)

