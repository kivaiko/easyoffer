from django.contrib import admin

from . import models
from .models import Mentor, Review

admin.site.register(models.Skill)
admin.site.register(models.Topic)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'surname', 'permission', 'public', 'telegram', 'created_at')
    search_fields = ('username',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'mentor', 'rating', 'public', 'created_at')