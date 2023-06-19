from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'main'),
    path('about-us', views.about, name = 'about'),
    path('create', views.create, name = 'create'),
    path('phones', views.phones),
]
