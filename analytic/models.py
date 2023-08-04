from django.db import models
from django.urls import reverse
from rating.models import Profession


class Skill(models.Model):
    class Meta:
        db_table = 'anaytics_skills'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.title, self.frequency


class KeyWord(models.Model):
    class Meta:
        db_table = 'anaytics_keywords'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.title, self.frequency