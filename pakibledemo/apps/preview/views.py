from django.shortcuts import render
from django.views.generic import TemplateView


class DemoTemplateView(TemplateView):
    template_name = 'demo.html'