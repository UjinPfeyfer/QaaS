from rest_framework import serializers


class ProgressSerializer(serializers.Serializer):
    totalNumberOfQuestions = serializers.IntegerField()
    passedNumberOfQuestions = serializers.IntegerField()
