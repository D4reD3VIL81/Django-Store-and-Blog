from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class DashboardView(TemplateView):
    template_name = "account/dashboard.html"

from .forms import *
from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = 'account-dashboard'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)