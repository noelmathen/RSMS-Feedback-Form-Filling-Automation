# feedback_app/serializers.py
from rest_framework import serializers

class FeedbackSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
