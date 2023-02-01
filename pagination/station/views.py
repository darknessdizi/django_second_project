from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as input_file:
        rdr = csv.DictReader(input_file)
        object_list = []
        for element in rdr:
            object_list.append(element)

    # with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as input_file:
    # paginator = Paginator(object_list, 10)
        # print('**1**', csv.reader(input_file))
        # for i in csv.reader(input_file):
        #     print(i)

    # page_number = int(request.GET.get("page", 1))
    # page = paginator.get_page(page_number)
 
    context = {
        'bus_stations': rdr,
        # 'page': page,
    }
    
    return render(request, 'station/index.html', context)
