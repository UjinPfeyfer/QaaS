from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..answerSerializer import AnswerSerializer
from ..models import Answer


class AnswersView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Answer.objects.all()

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search", None)
        if search is None:
            answers = Answer.objects.all()
        else:
            answers = Answer.objects.filter(text__contains=search)

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'text': request.data.get('text'),
            'question': request.data.get('question')
        }
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
