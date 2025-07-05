from django.urls import path
from countries import views

app_name = 'countries'
urlpatterns = [
    path('', views.home, name='home'),
    path('countries-list/', views.countries_list, name='countries-list'),
    path('languages/', views.language_list, name='language-list'),
    path('countries/<int:pk>/', views.country_detail, name='country-detail'),
    path('languages/<int:pk>/countries/', views.countries_by_language, name='countries-by-lang'),
    path('countries/letter/<str:letter>/', views.countries_by_letter, name='countries-by-letter'),
]