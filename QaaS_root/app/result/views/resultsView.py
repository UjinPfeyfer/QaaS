from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Result
from ..resultModel import ResultModel
from ..serializers.resultModelSerializer import ResultModelSerializer
from ..serializers.resultSerializer import ResultSerializer
from ...answer.models import Answer
from ...question.models import Question
from ...quiz.models import Quiz


class ResultsView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Result.objects.all()

    def get_object(self, quiz_id):
        try:
            return Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return None

    def get(self, request, quiz_id, *args, **kwargs):
        quiz = self.get_object(quiz_id)

        if not quiz:
            return Response(
                {"result": "Results do not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = request.user.id
        answers = Result.objects.filter(user=user).values_list('answer', flat=True)

        if not answers:
            return Response(
                {"result": "Results do not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        questions = Question.objects.filter(quiz_id=quiz)
        results = []
        for question in questions:
            result = ResultModel(question.text)
            user_answers = list(Answer.objects.filter(question=question.id, id__in=answers))
            result.answer = user_answers
            results.append(result)
        serializer = ResultModelSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        answers = request.data.get('answers')
        user = request.user.id
        for answer in answers:

            data = {
                'answer': answer,
                'user': user
            }
            serializer = ResultSerializer(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


