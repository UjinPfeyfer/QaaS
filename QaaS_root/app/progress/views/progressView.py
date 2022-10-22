from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Progress
from ..progressSerializer import ProgressSerializer
from ...answer.models import Answer
from ...question.models import Question
from ...result.models import Result


class ProgressView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Question.objects.all()

    def get_question_ids(self, quiz_id):
        return Question.objects.filter(quiz=quiz_id).values_list("id", flat=True)

    def get(self, request, quiz_id, *args, **kwargs):
        question_ids = self.get_question_ids(quiz_id)
        if not question_ids:
            return Response(
                {"result": "Result does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        all_answers = Answer.objects.filter(question__in=question_ids)
        passed_answers = Result.objects.filter(answer__in=all_answers, user=request.user.id)
        passed_questions = Answer.objects.filter(id__in=passed_answers).values_list("question", flat=True)
        progress = Progress(len(question_ids), len(passed_questions))
        serializer = ProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

