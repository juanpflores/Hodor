from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^$',
        TemplateView.as_view(
            template_name='prueba.html'
        ),
        name='prueba'
    ),
    url(
        r'^maya/$',
        TemplateView.as_view(
            template_name='landing-maya.html'
        ),
        name='maya'
    ),
    
]
