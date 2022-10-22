from django.db import models

from django.contrib.auth.models import User

from ..answer.models import Answer


class Result(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answerTime = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
