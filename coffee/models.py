from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, default="Methodical")

    def __str__(self):
        return self.name
