from django.db import models

# Create your models here.
class Document:
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    version = models.IntegerField()

