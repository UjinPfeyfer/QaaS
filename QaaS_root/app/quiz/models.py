from django.db import models

from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=80)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name
