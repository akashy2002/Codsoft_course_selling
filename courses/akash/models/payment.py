from django.db import models
from akash.models import UserCourse
from akash.models.registration_form import Registration
from akash.models import Course


class Payment(models.Model):
    order_id = models.CharField(max_length=50, null=False)
    payment_id = models.CharField(max_length=50)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_course = models.ForeignKey(
        UserCourse, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
