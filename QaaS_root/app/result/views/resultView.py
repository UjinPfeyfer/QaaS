from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Answer, Result
from ..resultModel import ResultModel
from ..serializers.resultModelSerializer import ResultModelSerializer

from ...question.models import Question


class ResultView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Result.objects.all()

    def get_user_result(question_id, user_id):
        answers = Answer.objects.filter(question=question_id).values_list('id', flat=True)
        result = Result.objects.filter(answer__in=answers, user=user_id).values_list('answer', flat=True)
        return Answer.objects.filter(id__in=result)

    def get(self, request, question_id, *args, **kwargs):
        user = request.user.id
        user_result = self.get_user_result(question_id, user)
        question = Question.objects.get(id=question_id)

        if not user_result:
            return Response(
                {"result": "Result does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        result = ResultModel(question)
        result.answer = user_result
        serializer = ResultModelSerializer(result)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, answer_id, *args, **kwargs):
        user = request.user.id
        results = self.get_user_result(answer_id, user)

        if not results:
            return Response(
                {"result": "Result does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for result in results:
            result.delete()

        return Response(
            {"result": "Result deleted"},
            status=status.HTTP_200_OK
        )
