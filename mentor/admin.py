from django.contrib import admin

from . import models

admin.site.register(models.Direction)
admin.site.register(models.Skill)
admin.site.register(models.Topic)
admin.site.register(models.PayMethod)
admin.site.register(models.Tag)
admin.site.register(models.Language)
admin.site.register(models.CountryExperienceOnline)
admin.site.register(models.CountryExperienceOffline)
admin.site.register(models.Mentor)