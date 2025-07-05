from django.urls import path
from countries import views

app_name = 'countries'
urlpatterns = [
    path('', views.home, name='home'),
    path('countries-list/', views.countries_list, name='countries-list'),
    path('countries/<str:country_name>/', views.country_detail, name='country-detail'),
]