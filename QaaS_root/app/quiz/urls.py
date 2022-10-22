from django.urls import path

from .views import QuizView
from .views import QuizzesView
from .views import QuizzesAllView
from ..result.views.resultsView import ResultsView

urlpatterns = [
    path('', QuizzesView.as_view()),
    path('/all', QuizzesAllView.as_view()),
    path('/<int:quiz_id>', QuizView.as_view()),
    path('/<int:quiz_id>/results', ResultsView.as_view()),
]