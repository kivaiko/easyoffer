from django.db import models
from django.utils import timezone
from django.urls import reverse


class Direction(models.Model):
    class Meta:
        db_table = 'directions'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Skill(models.Model):
    class Meta:
        db_table = 'mentor_skills'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Topic(models.Model):
    class Meta:
        db_table = 'topics'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class PayMethod(models.Model):
    class Meta:
        db_table = 'pay_methods'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta:
        db_table = 'mentor_tags'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Language(models.Model):
    class Meta:
        db_table = 'languages'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class CountryExperienceOnline(models.Model):
    class Meta:
        db_table = 'country_experience_online'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class CountryExperienceOffline(models.Model):
    class Meta:
        db_table = 'country_experience_offline'

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Mentor(models.Model):
    class Meta:
        db_table = 'mentors'

    STATUSES = [
        ('public', 'Public'),
        ('moderation', 'Moderation'),
        ('disabled', 'Disabled'),
    ]

    UTC = [
        ('UTC−12', 'UTC−12'),
        ('UTC−11', 'UTC−11'),
        ('UTC−10', 'UTC−10'),
        ('UTC−9', 'UTC−9'),
        ('UTC−8', 'UTC−8'),
        ('UTC−7', 'UTC−7'),
        ('UTC−6', 'UTC−6'),
        ('UTC−5', 'UTC−5'),
        ('UTC−4', 'UTC−4'),
        ('UTC−3', 'UTC−3'),
        ('UTC−2', 'UTC−2'),
        ('UTC−1', 'UTC−1'),
        ('UTC+0', 'UTC+0'),
        ('UTC+1', 'UTC+1'),
        ('UTC+2', 'UTC+2'),
        ('UTC+3', 'UTC+3'),
        ('UTC+4', 'UTC+4'),
        ('UTC+5', 'UTC+5'),
        ('UTC+6', 'UTC+6'),
        ('UTC+7', 'UTC+7'),
        ('UTC+8', 'UTC+8'),
        ('UTC+9', 'UTC+9'),
        ('UTC+10', 'UTC+10'),
        ('UTC+11', 'UTC+11'),
        ('UTC+12', 'UTC+12'),
        ('UTC+13', 'UTC+13'),
        ('UTC+14', 'UTC+14'),
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.SlugField(max_length=255)
    UTC = models.CharField(max_length=100, choices=UTC, default='UTC+0')
    profession = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)
    topics = models.ManyToManyField(Topic)
    directions = models.ManyToManyField(Direction)
    pay_methods = models.ManyToManyField(PayMethod)
    tags = models.ManyToManyField(Tag, blank=True)
    languages = models.ManyToManyField(Language)
    country_Experience_online = models.ManyToManyField(CountryExperienceOnline)
    country_Experience_offline = models.ManyToManyField(CountryExperienceOffline)
    experience = models.PositiveIntegerField()
    cost_30m = models.PositiveIntegerField()
    cost_1h = models.PositiveIntegerField()
    cv_link = models.URLField(blank=True)
    about_me = models.TextField()
    telegram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField()
    portfolio = models.URLField(blank=True)
    priority = models.BooleanField()
    public = models.BooleanField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} {self.surname} – {self.username}"

    def get_mentor_url(self):
        return reverse('mentor', args=[self.username])
