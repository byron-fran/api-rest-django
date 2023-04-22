from django.db import models

# Create your models here.
class Project (models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    technolody = models.TextField()
    created_at = models.DateTimeField(auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_created=True, null=True)
