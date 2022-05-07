from django.db import models

# Create your models here.


class Question(models.Model):
    question_id = models.PositiveIntegerField(null=True)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    time_create = models.DateTimeField(auto_now_add=True)


class QuestionNumber(models.Model):
    settings = models.PositiveIntegerField(null=True)