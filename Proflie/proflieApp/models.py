from django.db import models


class messgae(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
