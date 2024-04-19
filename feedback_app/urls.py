# feedback_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.FeedbackAPIView.as_view(), name='feedback-api'),
]
