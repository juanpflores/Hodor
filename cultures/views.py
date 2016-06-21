from django.shortcuts import get_object_or_404

from django.db.models import Q

from django.views.generic import(
    ListView,
    DetailView,
    TemplateView
)

from .models import (
    Culture,
    God,
    Temple,
    Museum,
    CultureHasPeriod,
)


class LandingView(ListView):
    template_name = 'landing.html'
    model = Culture

    def get_queryset(self):
        queryset = self.queryset
        q = self.request.GET.get('q', None)
        if q is not None:
            queryset = Culture.objects.filter(
                Q(name__icontains=q) | Q(summary__icontains=q) |
                Q(religion__name__icontains=q) | Q(religion__description__icontains=q) |  # NOQA
                Q(region__name__icontains=q) | Q(region__country__name__icontains=q) |  # NOQA
                Q(region__description__icontains=q)
            )
            return queryset
        else:
            return queryset


class AdventureView(DetailView):

    context_object_name = 'culture'
    template_name = 'landing-maya.html'
    model = Culture

    def get_object(self):
        culture = get_object_or_404(Culture, name__icontains=self.kwargs['name'])  # NOQA
        return culture

    def get_context_data(self, **kwargs):
        context = super(AdventureView, self).get_context_data(**kwargs)
        context['gods'] = God.objects.filter(culture=self.get_object().pk)
        context['temples'] = Temple.objects.filter(culture=self.get_object().pk)  # NOQA
        context['museums'] = Museum.objects.filter(cultures=self.get_object().pk)  # NOQA
        context['periods'] = CultureHasPeriod.objects.filter(culture=self.get_object().pk).order_by('pk')  # NOQA
        return context
