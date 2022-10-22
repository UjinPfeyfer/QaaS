from django.contrib import admin
from django.urls import path, include

from app.quiz import urls as quiz_urls
from app.question import urls as question_urls
from app.answer import urls as answer_urls
from app.assignee import urls as assignee_urls
from app.progress import urls as progress_urls
from app.email import urls as email_urls

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('quiz', include(quiz_urls)),
    path('question', include(question_urls)),
    path('answer', include(answer_urls)),
    path('assignee', include(assignee_urls)),
    path('progress', include(progress_urls)),
    path('email', include(email_urls))
]

