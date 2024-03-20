import json

from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from sensors.black_list import BLACK_LIST_IP
from sensors.forms import Feedback
from sensors.models import Sensor, Client

from django.core.mail import send_mail
from django.utils.timezone import now


def get_client_ip(request):
    """
    Get user's IP
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
    return ip


def send_email_to_admin(content, to_email="septicmasterpro.msk@gmail.com"):
    send_mail(
        "Сообщение от api-manager",
        content,
        'api@izi-start.ru',
        [
            to_email
        ],
        fail_silently=True,
        html_message=content + now().strftime("%d/%m/%Y - %H:%M:%S")
    )


# @api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# def sensor(request):
#     client_ip = get_client_ip(request)
#     if client_ip in BLACK_LIST_IP:
#         return Response({'detail': 'Access denied!'})
#     if request.method == 'POST':
#         data = list(request.POST.keys())[0]
#         sensor_data = json.loads(data)
#         print(sensor_status := sensor_data['sensor_status'])
#         print(mac_address := sensor_data['mac_address'])
#         sensor_item = Sensor.objects.filter(sensor_MAC=mac_address).first()
#         to_email = sensor_item.sensor_email
#         if sensor_status != sensor_item.sensor_status:
#             send_email_to_admin(
#                 f"Сработал датчик {sensor_item.sensor_description}: статус {sensor_status}, устройство {mac_address}   ", to_email)
#         sensor_item.sensor_status = sensor_status
#         sensor_item.sensor_status_change = now().strftime("%d/%m/%Y - %H:%M:%S")
#         sensor_item.save()
#         return Response(sensor_data)
#     return Response({'detail': 'connected'})


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def sensor(request):
    client_ip = get_client_ip(request)
    if client_ip in BLACK_LIST_IP:
        return Response({'detail': 'Access denied!'})
    if request.method == 'POST':
        sensor_data = request.data
        print(sensor_status := sensor_data['sensor_status'])
        print(mac_address := sensor_data['mac_address'])
        sensor_item = Sensor.objects.filter(sensor_MAC=mac_address).first()
        to_email = sensor_item.sensor_email
        if sensor_status != sensor_item.sensor_status:
            send_email_to_admin(
                f"Сработал датчик {sensor_item.sensor_description}: статус {sensor_status}, устройство {mac_address}   ", to_email)
        sensor_item.sensor_status = sensor_status
        sensor_item.sensor_status_change = now().strftime("%d/%m/%Y - %H:%M:%S")
        sensor_item.save()
        return Response(sensor_data)
    return Response({'detail': 'connected'})


def feedback(request):
    global client_name, client_phone
    if request.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            client_name = form.data['name']
            client_phone = form.data['phone']
        client_ip = get_client_ip(request)
        link = request.META.get('HTTP_REFERER')
        try:
            client = Client(client_name=client_name,
                            client_phone=client_phone,
                            client_ip_address=client_ip)
            client.save()
            send_email_to_admin(f"E-mail от клиента: {client_name}, номер телефона: {client_phone}, со страницы {link}, IP {client_ip}  ")
            return render(request, 'index.html')
        except:
            send_email_to_admin(
                f"Повторное обращение от клиента: {client_name}, номер телефона: {client_phone}, со страницы {link}, IP {client_ip}   ")
            return render(request, 'index.html')
    return render(request, 'index.html')
