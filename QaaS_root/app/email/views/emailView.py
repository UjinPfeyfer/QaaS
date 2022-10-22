from django.core.mail import send_mail, BadHeaderError
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmailView(APIView):
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return None

    def post(self, request, answer_id, *args, **kwargs):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return Response(
                    {"result": "Invalid header found"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {"result": "Email sent"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"result": "Make sure all fields are correct"},
                status=status.HTTP_400_BAD_REQUEST
            )
