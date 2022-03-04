from multiprocessing import parent_process
from django.db import models
from django.conf import settings
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    max_student = models.IntegerField(default=0)
    statr_date = models.DateField()
    end_date = models.DateField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_enroll')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_student')