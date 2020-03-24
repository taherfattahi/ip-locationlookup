import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index1(request, format=None):
    if request.method == 'GET':
        url = 'https://api.ipgeolocation.io/ipgeo?apiKey=2a471cfb9b14427d936774a6f660fd4d&ip={}'
        ip = get_client_ip(request)
        if ip:
            r = requests.get(url.format(ip)).json()

        return Response(r)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip