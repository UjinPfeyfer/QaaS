from rest_framework import serializers

from ..models import Question
from ...answer.answerSerializer import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "text", "quiz", "answers"]
