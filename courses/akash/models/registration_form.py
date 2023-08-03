from django.db import models


class Registration(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=50, )
    password2 = models.CharField(max_length=50,)

    def __str__(self):
        return self.username
