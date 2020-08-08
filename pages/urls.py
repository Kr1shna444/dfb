from django.urls import path
from .views import HomePageView, AboutPageView, BasePageView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPageView.as_view(), name = 'about'),
path('base/', AboutPageView.as_view(), name = 'base'),
]
