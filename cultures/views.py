from django.shortcuts import get_object_or_404

from django.views.generic import(
    ListView,
    DetailView,
    TemplateView
)

from .models import (
    Language,
    Religion,
    Culture,
    God,
    Temple,
    Museum
)


class LandingView(ListView):
    template_name = 'prueba.html'
    model = Culture


class AdventureView(DetailView):
    template_name = 'landing-maya.html'
    model = Culture

    def get_object(self):
        culture = get_object_or_404(Culture, name=self.kwargs['name'])
        return culture

    def get_context_data(self, **kwargs):
        context = super(AdventureView, self).get_context_data(**kwargs)
        return context
