from django.contrib import admin

from . import models

admin.site.register(models.Profession)
admin.site.register(models.Tag)
admin.site.register(models.Question)
admin.site.register(models.Comment)
admin.site.register(models.Link)
admin.site.register(models.Rating)
admin.site.register(models.MockInterview)
admin.site.register(models.Skill)
admin.site.register(models.KeyWord)