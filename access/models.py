from django.db import models
from django.utils import timezone


class Access(models.Model):
    class Meta:
        db_table = 'accesses'

    ip_address = models.CharField(max_length=20)
    delete_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.ip_address
