from django.db import models

class vids(models.Model):
    filename=models.CharField(max_length=200)
    filesize = models.FloatField()
    duration = models.FloatField()
    filetype=models.CharField(max_length=6)
    up_date=models.DateTimeField('date uploaded', auto_now_add=True)