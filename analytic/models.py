from django.db import models
from django.urls import reverse
from rating.models import Profession



"""class Profession(models.Model):
    class Meta:
        db_table = 'analytic_professions'

    title = models.CharField(max_length=255)
    prof_slug = models.SlugField(max_length=255)
    public_status = models.BooleanField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('profession', args=[self.prof_slug])"""


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