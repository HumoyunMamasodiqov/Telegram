from django.db import models


class Odam(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.name
