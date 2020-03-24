from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import os


def index(request):

    try:
        # print(settings)
        with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
            return HttpResponse(file.read())

    except :
        return HttpResponse(
            """
            index.html not found ! build your React app !!
            """,
            status=501,)
