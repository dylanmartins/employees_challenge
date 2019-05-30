from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    created_date = models.DateTimeField(
            default=timezone.now)