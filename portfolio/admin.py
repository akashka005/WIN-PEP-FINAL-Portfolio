from django.contrib import admin
from .models import Skill, Project, Achievement, Education, ContactMessage

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    list_filter = ('status',)
    search_fields = ('title', 'tech_stack')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'date_range')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at')
    readonly_fields = ('created_at',)