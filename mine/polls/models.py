from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
import datetime


class Question (models.Model):
    question_text=models.CharField(max_length=200)
    pu_date=models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.question_text
        
    def was_pulished_rescently(self):
        return timezone.now()-datetime.timedelta(days=1) <=self.pu_date <= timezone.now()
        

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def _str_(self):
        return self.choice_text


class Stat(models.Model):
    category_count = models.IntegerField()


# Create your models here.
