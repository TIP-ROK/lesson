from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    description = models.TextField()
    pub_date = models.DateTimeField("date published")

