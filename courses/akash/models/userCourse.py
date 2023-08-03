from django.db import models
from akash.models.registration_form import Registration
from akash.models import Course


class UserCourse(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
