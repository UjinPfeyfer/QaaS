from rest_framework import serializers

from ...answer.answerSerializer import AnswerSerializer
from ...question.models import Question


class ResultsSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "text", "quiz", "answers"]
