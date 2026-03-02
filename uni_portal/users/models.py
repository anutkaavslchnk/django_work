from django.db import models

# Create your models here.


class User(models.Model):
    ROLES=[
        ("teacher","Teacher"),
        ("student","Student"),
    ]
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    role=models.CharField(max_length=10, choices=ROLES)
    age=models.IntegerField()