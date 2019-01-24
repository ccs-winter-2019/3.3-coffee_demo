from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from . import models


class HomeView(TemplateView):
    template_name = 'coffee/home.html'

    def get_context_data(self, **kwargs):
        good_coffees = models.Coffee.objects.filter(origin='Methodical')

        context = {
            'coffees': good_coffees
        }

        return context


class CoffeeDetailView(DetailView):
    template_name = 'coffee/detail.html'
    model = models.Coffee
