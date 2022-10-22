from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Quiz

from ..serializers.quizzesSerializer import QuizzesSerializer


class QuizzesView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Quiz.objects.all()

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search", None)
        if search is None:
            quizes = Quiz.objects.filter(creator=request.user.id)
        else:
            quizes = Quiz.objects.filter(creator=request.user.id, name__contains=search)

        serializer = QuizzesSerializer(quizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
