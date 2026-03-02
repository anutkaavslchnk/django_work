from django.db import models
from users.models import User
# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    teacher=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="the related teacher")
    max_students=models.IntegerField()


class Enrollment(models.Model):
    CHOICES=[
        ("pending","Pending"),       
        ("accepted","Accepted"),
        ("rejected","Rejected")
    ]
    
    student=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="the related student")
    project=models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name="the related project")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20, choices=CHOICES, default='pending')


class Submission(models.Model):
    enrollment=models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name="the related enrollment")
    file=models.FileField(upload_to="submissions/")
    submitted_at=models.DateTimeField(auto_now_add=True)
