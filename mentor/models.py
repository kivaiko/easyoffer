from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Direction(models.Model):
    class Meta:
        db_table = 'directions'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Skill(models.Model):
    class Meta:
        db_table = 'skills'

    title = models.CharField(max_length=30)
    directions = models.ManyToManyField(Direction, blank=False)

    def __str__(self):
        return self.title


class Topic(models.Model):
    class Meta:
        db_table = 'topics'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Mentor(models.Model):
    class Meta:
        db_table = 'mentors'

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.SlugField(max_length=255)
    profession = models.CharField(max_length=50)
    topics = models.ManyToManyField(Topic)
    skills = models.ManyToManyField(Skill)
    about_me = models.TextField(blank=True)
    directions = models.ManyToManyField(Direction, blank=False)
    experience = models.PositiveIntegerField(blank=False)
    cost_30m = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(500)])
    cost_1h = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1000)])
    telegram = models.CharField(max_length=100, blank=False)
    instagram = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=False)
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)
    website = models.URLField(blank=True)
    priority = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)
    image = models.FileField(upload_to='mentors_images')

    def __str__(self):
        return f"{self.name} {self.surname} – {self.username}"

    def get_mentor_url(self):
        return reverse('mentor', args=[self.username])


class Review(models.Model):
    class Meta:
        db_table = 'reviews'

    GRADE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    author = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=GRADE)
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.author}, {self.mentor}'
