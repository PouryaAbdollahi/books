from django.urls import path
from pages.views import HomePageView, AboutUsPageView


app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutUsPageView.as_view(), name='about')
]
