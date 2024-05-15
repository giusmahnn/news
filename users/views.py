from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.http import HttpResponse


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    email_from = 'your-email@gmail.com'
    recipient_list = ['recipient@example.com']
    
    send_mail(subject, message, email_from, recipient_list)
    
    return HttpResponse('Email sent successfully!')
