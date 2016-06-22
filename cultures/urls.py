from django.conf.urls import url

from cultures.views import(
    LandingView,
    AdventureView,
)

urlpatterns = [

    url(
        r'^$',
        LandingView.as_view(),
        name='landing'
    ),

    url(
        r'^culturas/(?P<name>[a-zA-Z]+)/$',
        AdventureView.as_view(),
        name='adventure'
    ),

]
