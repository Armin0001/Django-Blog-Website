# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from users.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #voter = models.ForeignKey(User, on_delete=models.CASCADE)
    #voted = models.ManyToMany(User)

    def __str__(self):
        return self.choice_text

class Voter(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    poll = models.ForeignKey(Question, on_delete = models.CASCADE)

# class Voter(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     option = models.ForeignKey(Choice, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ['option', 'user']

# class Voter(models.Model):
#     user = models.ForeignKey(User)
#     choice = models.ForeignKey(Law)



