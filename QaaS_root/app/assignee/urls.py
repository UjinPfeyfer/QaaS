from django.urls import path

from ..assignee.views.assigneeView import AssigneeView

urlpatterns = [
    path('', AssigneeView.as_view()),
    path('/<int:quiz_id>', AssigneeView.as_view())
]