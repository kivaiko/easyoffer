from django.db import models
from django.utils import timezone
from django.urls import reverse


class Profession(models.Model):
    class Meta:
        db_table = 'professions'

    title = models.CharField(max_length=255)
    prof_slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('profession', args=[self.prof_slug])


class Teg(models.Model):
    class Meta:
        db_table = 'tegs'

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        db_table = 'questions'

    STATUSES = [
        ('public', 'public'),
        ('moderation', 'moderation'),
        ('disabled', 'disabled'),
    ]

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUSES, default='public')
    rating_qty = models.IntegerField(default=1)
    comments_qty = models.IntegerField(default=0)
    links_qty = models.IntegerField(default=0)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', args=[self.id])


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50)
    rating_qty = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author