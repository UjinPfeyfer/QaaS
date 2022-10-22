from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Question
from ..serializers.questionSerializer import QuestionSerializer


class QuestionView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Question.objects.all()

    def get_object(self, question_id):
        try:
            return Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return None

    def get(self, request, question_id, *args, **kwargs):
        question = self.get_object(question_id)
        if not question:
            return Response(
                {"result": "Question does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, question_id, *args, **kwargs):
        question = self.get_object(question_id)
        if not question:
            return Response(
                {"result": "Question does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'text': request.data.get('text'),
            'quiz': request.data.get('quiz')
        }
        serializer = QuestionSerializer(instance=question, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id, *args, **kwargs):
        question = self.get_object(question_id)
        if not question:
            return Response(
                {"result": "Question does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        question.delete()
        return Response(
            {"result": "Question deleted"},
            status=status.HTTP_200_OK
        )
