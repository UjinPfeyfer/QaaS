from django.urls import path

from .views import ProgressView

urlpatterns = [
    path('/<int:quiz_id>', ProgressView.as_view()),
]
