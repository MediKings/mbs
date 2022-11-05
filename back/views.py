from django.shortcuts import render
from django.views.generic.edit import CreateView
from home.models import Serie
from .forms import SerieForm


class AddSerie(CreateView):
    model = Serie
    form_class = SerieForm
    template_name = 'back/add-serie.html'
    success_url = '/'
