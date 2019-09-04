from django.db import models


# Create your models here.
from django.utils.timezone import localtime


class Tenant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    due_date = models.DateField(default=localtime)

    def to_dict(self):
        return {
            'name': self.name,
            'dueDate': str(self.due_date),
            'id': self.pk,
        }
