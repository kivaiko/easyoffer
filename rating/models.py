from django.db import models
from django.utils import timezone
from django.urls import reverse


class Profession(models.Model):
    class Meta:
        db_table = 'professions'

    STATUSES = [
        ('public', 'Public'),
        ('disabled', 'Disabled'),
    ]

    title = models.CharField(max_length=255)
    prof_slug = models.SlugField(max_length=255)
    status = models.CharField(max_length=100, choices=STATUSES, default='disabled')
    description = models.TextField(max_length=500, default='212')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('profession', args=[self.prof_slug])

    def get_url_quiz(self):
        return reverse('quiz', args=[self.prof_slug])


class Tag(models.Model):
    class Meta:
        db_table = 'tags'

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        db_table = 'questions'

    GRADES = [
        ('without', 'Without'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    title = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100, choices=GRADES, default='without')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', args=[self.id])


class Rating(models.Model):
    class Meta:
        db_table = 'ratings'

    STATUSES = [
        ('public', 'Public'),
        ('moderation', 'Moderation'),
        ('disabled', 'Disabled'),
    ]

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=1)
    status = models.CharField(max_length=100, choices=STATUSES, default='moderation')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.profession}, {self.question}"


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    STATUSES = [
        ('public', 'Public'),
        ('moderation', 'Moderation'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50)
    short_rating = models.IntegerField(default=1)
    long_rating = models.IntegerField(default=1)
    status = models.CharField(max_length=100, choices=STATUSES, default='moderation')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author


class VideoAnswerLink(models.Model):
    class Meta:
        db_table = 'video_answer_links'

    STATUSES = [
        ('public', 'Public'),
        ('moderation', 'Moderation'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    status = models.CharField(max_length=100, choices=STATUSES, default='moderation')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class ExtraContentLink(models.Model):
    class Meta:
        db_table = 'extra_content_links'

    STATUSES = [
        ('public', 'Public'),
        ('moderation', 'Moderation'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    status = models.CharField(max_length=100, choices=STATUSES, default='moderation')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class MockInterview(models.Model):
    class Meta:
        db_table = 'mock_interviews'

    STATUSES = [
        ('public', 'Public'),
        ('moderation', 'Moderation'),
        ('disabled', 'Disabled'),
    ]

    GRADES = [
        ('without', 'Without'),
        ('trainee', 'Trainee'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    url = models.URLField()
    status = models.CharField(max_length=100, choices=STATUSES, default='moderation')
    grades = models.CharField(max_length=100, choices=GRADES, default='without')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Skill(models.Model):
    class Meta:
        db_table = 'skills'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    frequency = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title, self.frequency


class KeyWord(models.Model):
    class Meta:
        db_table = 'keywords'

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    frequency = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title, self.frequency