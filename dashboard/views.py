from django.shortcuts import render


def dashboardView(request):
    return render(request, 'dashboard.html')


def loginView(request):
    pass
