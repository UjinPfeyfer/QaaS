from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..assigneeSerializer import AssigneeSerializer
from ..models import Assignee


class AssigneeView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Assignee.objects.all()

    def get_object(self, quiz_id, user_id):
        try:
            return Assignee.objects.get(user=user_id, quiz=quiz_id)
        except Assignee.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        user = request.user.id
        assignee = Assignee.objects.filter(user=user)
        serializer = AssigneeSerializer(assignee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'quiz': request.data.get('quiz'),
            'user': request.user.id
        }
        serializer = AssigneeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, quiz_id, *args, **kwargs):
        user = request.user.id
        assignee = self.get_object(quiz_id, user)

        if not assignee:
            return Response(
                {"result": "Assignee does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        assignee.delete()
        return Response(
            {"result": "Assignee deleted"},
            status=status.HTTP_200_OK
        )
