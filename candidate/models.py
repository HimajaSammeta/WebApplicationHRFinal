from django.db import models

class Feedback(models.Model):
    canid = models.IntegerField()
    cname = models.CharField(max_length=100)
    feedback = models.CharField(max_length=1000)
    feedbackdt = models.CharField(max_length=50)
    class Meta:
        db_table="feedback"

