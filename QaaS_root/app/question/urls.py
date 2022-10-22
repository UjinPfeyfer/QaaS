from django.urls import path

from .views import QuestionView
from .views import QuestionsView
from ..result.views.resultView import ResultView

urlpatterns = [
    path('', QuestionsView.as_view()),
    path('/<int:question_id>', QuestionView.as_view()),
    path('/<int:question_id>/result', ResultView.as_view()),
]