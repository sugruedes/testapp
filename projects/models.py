from django.db import models

# Create your models here.
# This is really just a table name, and a definition of the fields.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    images = models.FileField(upload_to="project_images/", blank=True)
