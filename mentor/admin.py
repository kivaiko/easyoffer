from django.contrib import admin

from . import models

admin.site.register(models.Direction)
admin.site.register(models.Topic)
admin.site.register(models.Mentor)