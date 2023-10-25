from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from users.models import User
from rating.models import Profession
from django.core.validators import MaxValueValidator


class Skill(models.Model):
    class Meta:
        db_table = 'skills'

    title = models.CharField(max_length=30)
    profession = models.ManyToManyField(Profession, blank=False)

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    topics = models.ManyToManyField(Topic)
    skills = models.ManyToManyField(Skill)
    description = models.CharField(max_length=100)
    about_me = RichTextField()
    profession = models.ManyToManyField(Profession, blank=False)
    experience = models.PositiveIntegerField(blank=False, default=1, validators=[MaxValueValidator(30)])
    cost_30m = models.PositiveIntegerField(blank=False, default=0, validators=[MaxValueValidator(50000)])
    cost_1h = models.PositiveIntegerField(blank=False, default=0, validators=[MaxValueValidator(50000)])
    telegram = models.CharField(max_length=100, blank=False)
    instagram = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)
    website = models.URLField(blank=True)
    priority = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    permission = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)
    last_update = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='mentors_images')

    def get_mentor_url(self):
        return reverse('mentor', args=[self.username])


class Review(models.Model):
    class Meta:
        db_table = 'reviews'

    GRADE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    author = models.CharField(max_length=30)
    text = RichTextField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.author}, {self.mentor}'
