from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Question

from ..serializers.questionsSerializer import QuestionsSerializer


class QuestionsView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Question.objects.all()

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search", None)
        if search is None:
            questions = Question.objects.all()
        else:
            questions = Question.objects.filter(text__contains=search)

        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'text': request.data.get('text'),
            'quiz': request.data.get('quiz')
        }
        serializer = QuestionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
