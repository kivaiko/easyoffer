from django.db import models
from django.urls import reverse
from rating.models import Profession
from django.utils import timezone


class Search(models.Model):
    class Meta:
        db_table = 'searches'

    title = models.CharField(max_length=255)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    url = models.URLField(max_length=5000)
    amount_vacancies = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    last_update = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} – {self.profession}"


class Skill(models.Model):
    class Meta:
        db_table = 'anaytics_skills'

    title = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    search = models.ForeignKey(Search, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} – {self.amount} – {self.search}"


class KeyWord(models.Model):
    class Meta:
        db_table = 'anaytics_keywords'

    title = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    search = models.ForeignKey(Search, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} – {self.amount} – {self.search}"