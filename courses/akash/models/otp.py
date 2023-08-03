from django.db import models
from akash.models.registration_form import Registration


class Profile(models.Model):
    user = models.OneToOneField(Registration, on_delete=models.CASCADE)
    mob = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
