from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from cultures import urls as cultures_urls
from quizzes import urls as quizzes_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(
        '',
        include(
            cultures_urls,
            namespace='cultures'
        )
    ),

    url(
        '',
        include(
            quizzes_urls,
            namespace='quizzes'
        )
    ),
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
    url(
        r'^sistema-solar/$',
        TemplateView.as_view(
            template_name='solar.html'
        ),
        name='solar'
    ),
]
