import unittest

from rest_framework import serializers

from ..answer.models import Answer

if __name__ == '__main__':
    unittest.main()

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text", "question", "correct"]

