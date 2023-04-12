from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Question, Answer, Code

# Create your views here.

class HomeView(TemplateView):
    template_name = 'codeisc/home.html'

    def get_contex_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
