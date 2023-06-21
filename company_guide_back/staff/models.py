from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    responsibilities = models.CharField(max_length=1000)