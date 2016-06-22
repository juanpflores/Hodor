from django.conf.urls import url

from quizzes.views import QuizView


urlpatterns = [

    url(
        r'^culturas/(?P<name>[a-zA-Z]+)/preguntas/$',
        QuizView.as_view(),
        name='list'
    ),
]
