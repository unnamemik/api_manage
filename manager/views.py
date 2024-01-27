from django.shortcuts import render

from manager.cities_dict import CITIES_DICT


def manager(request):
    host_name = request.get_host().split('.')[0].lower()
    geocity1 = CITIES_DICT[host_name][1]
    return render(request, 'manager.html', {'geocity1': geocity1})
