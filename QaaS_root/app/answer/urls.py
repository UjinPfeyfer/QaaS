from django.urls import path

from .views import AnswerView
from .views import AnswersView

urlpatterns = [
    path('', AnswersView.as_view()),
    path('/<int:answer_id>', AnswerView.as_view()),
]