from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    class Meta:
        db_table = 'tags'

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Profession(models.Model):
    class Meta:
        db_table = 'professions'

    title = models.CharField(max_length=255)
    prof_slug = models.SlugField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=False)
    public_rating = models.BooleanField()
    public_mock = models.BooleanField()
    public_analytic = models.BooleanField()
    description = models.TextField(max_length=500)
    telegram_chat = models.URLField()
    votes = models.PositiveIntegerField()
    votes_access = models.BooleanField()

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question_rating', args=[self.prof_slug])

    def get_url_quiz(self):
        return reverse('quiz', args=[self.prof_slug])

    def get_url_analytic(self):
        return reverse('analytic', args=[self.prof_slug])


class Question(models.Model):
    class Meta:
        db_table = 'questions'

    title = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100, choices=settings.GRADES, default='Не указан')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', args=[self.id])


class Rating(models.Model):
    class Meta:
        db_table = 'ratings'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=1)
    position = models.IntegerField(default=1000)
    public = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.profession}, {self.question}"


class Answer(models.Model):
    class Meta:
        db_table = 'comments'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50)
    rating = models.IntegerField(default=1)
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author


class VideoAnswerLink(models.Model):
    class Meta:
        db_table = 'video_answer_links'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    public = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class ExtraContentLink(models.Model):
    class Meta:
        db_table = 'extra_content_links'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class MockInterview(models.Model):
    class Meta:
        db_table = 'mock_interviews'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=600)
    url = models.URLField()
    public = models.BooleanField(default=True)
    grade = models.CharField(max_length=100, choices=settings.GRADES, default='Не указан')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} – {self.profession} – {self.public}"