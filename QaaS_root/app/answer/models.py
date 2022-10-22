from django.db import models

from ..question.models import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    text = models.TextField()
    correct = models.BooleanField(default=False)
    answerTime = models.TimeField(auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.text
