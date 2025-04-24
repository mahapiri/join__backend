from django.shortcuts import render


def homeView(request):
    return render(request, "join/base.html")