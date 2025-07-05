import json

from django.http import Http404
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def countries_list(request):
    json_path = 'countries.json'

    with open(json_path, encoding='utf-8') as f:
        countries = json.load(f)

    context = {
        'countries': countries,
    }

    return render(request, 'countries-list.html', context=context)

def country_detail(request, country_name=None):
    json_path = 'countries.json'

    with open(json_path, encoding='utf-8') as f:
        countries = json.load(f)

    country = None
    for c in countries:
        if c['country'].lower() == country_name.lower():
            country = c
            break

    if country is None:
        raise Http404("Country not found")

    context = {
        'country': country,
    }

    return render(request, 'country-detail.html', context=context)

def language_list(request):
    json_path = 'countries.json'
    with open(json_path, encoding='utf-8') as f:
        countries = json.load(f)

    all_languages = []
    for country in countries:
        all_languages.extend(country['languages'])

    unique_languages = list(set(all_languages))

    context = {
        'languages': unique_languages,
    }

    return render(request, 'languages.html', context=context)