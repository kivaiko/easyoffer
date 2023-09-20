from django.db import models


class CustomUser(models.Model):
    class Meta:
        db_table = 'custom_users'

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email

