from django.db import models


class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
