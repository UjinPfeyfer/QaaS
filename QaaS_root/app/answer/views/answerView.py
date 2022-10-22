from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Answer

from ..answerSerializer import AnswerSerializer


class AnswerView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Answer.objects.all()

    def get_object(self, answer_id):
        try:
            return Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            return None

    def get(self, request, answer_id, *args, **kwargs):
        answer = self.get_object(answer_id)
        if not answer:
            return Response(
                {"result": "Answer does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, answer_id, *args, **kwargs):
        answer = self.get_object(answer_id)
        if not answer:
            return Response(
                {"result": "Answer does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'text': request.data.get('text'),
            'question': request.data.get('question')
        }
        serializer = AnswerSerializer(instance=answer, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_id, *args, **kwargs):
        answer = self.get_object(answer_id)
        if not answer:
            return Response(
                {"result": "Answer does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        answer.delete()
        return Response(
            {"result": "Answer deleted"},
            status=status.HTTP_200_OK
        )
