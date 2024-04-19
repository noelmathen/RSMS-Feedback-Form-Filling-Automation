# feedback_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from .feedback_script import run_feedback_script

class FeedbackAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            feedback_messages = run_feedback_script(username, password)
            return Response({'feedback_messages': feedback_messages})
        else:
            return Response(serializer.errors, status=400)
