from django.contrib import admin

from . import models
from .models import Search

admin.site.register(models.Skill)
admin.site.register(models.KeyWord)


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'profession', 'amount_vacancies', 'public', 'last_update')