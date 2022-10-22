from django.contrib import admin

from .answer.models import Answer
from .assignee.models import Assignee
from .question.models import Question
from .quiz.models import Quiz
from .result.models import Result

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Assignee)
