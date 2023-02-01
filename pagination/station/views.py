from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as input_file:
        object_list = [i for i in csv.DictReader(input_file)]

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(object_list, 10)
    page = paginator.get_page(page_number)

    context = {
                'bus_stations': page,
                'page': page,
            } 
    return render(request, 'station/index.html', context) 
 