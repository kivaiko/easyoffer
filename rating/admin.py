from django.contrib import admin

from . import models

admin.site.register(models.Profession)
admin.site.register(models.Teg)
admin.site.register(models.Question)
admin.site.register(models.Comment)