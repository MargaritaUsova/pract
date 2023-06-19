from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about-us', views.about, name = 'about'),
    path('create', views.create, name = 'create'),
    path('phones', views.phones),
    path('laptops', views.laptops),
    path('appliances', views.byt_techn),
    path('computers', views.computers),
    path('tablets', views.tablets),
    path('smart_speakers', views.smart_speakers),
]
