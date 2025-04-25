

from django.http import HttpResponse


def contactView(request):
    return HttpResponse('Hallo')