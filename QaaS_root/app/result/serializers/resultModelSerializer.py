from rest_framework import serializers

from ...answer.answerSerializer import AnswerSerializer


class ResultModelSerializer(serializers.Serializer):
    question = serializers.CharField()
    answer = AnswerSerializer(many=True)
