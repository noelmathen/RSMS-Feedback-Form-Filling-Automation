#views.py
from django.shortcuts import render
from .forms import FeedbackForm
from .feedback_script import run_feedback_script

def feedback_form(request):
    feedback_messages = []

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            feedback_messages = run_feedback_script(username, password)
    else:
        form = FeedbackForm()

    return render(request, 'feedback_app/index.html', {'form': form, 'feedback_messages': feedback_messages})
