from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Quiz

from ..serializers.quizSerializer import QuizSerializer


class QuizView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Quiz.objects.all()

    def get_object(self, quiz_id):
        try:
            return Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return None

    def get(self, request, quiz_id, *args, **kwargs):
        quiz = self.get_object(quiz_id)
        if not quiz:
            return Response(
                {"result": "Quiz does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, quiz_id, *args, **kwargs):
        quiz = self.get_object(quiz_id)
        if not quiz:
            return Response(
                {"result": "Quiz does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'creator': request.user.id
        }
        serializer = QuizSerializer(instance=quiz, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, quiz_id, *args, **kwargs):
        quiz = self.get_object(quiz_id)
        if not quiz:
            return Response(
                {"result": "Quiz does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        quiz.delete()
        return Response(
            {"result": "Quiz deleted"},
            status=status.HTTP_200_OK
        )
