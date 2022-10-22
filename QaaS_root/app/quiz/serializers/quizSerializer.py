from rest_framework import serializers

from app.quiz.models import Quiz
from ...question.serializers.questionSerializer import QuestionSerializer


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ["id", "name", "creator", "createTime", "questions"]
