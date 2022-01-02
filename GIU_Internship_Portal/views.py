from django.shortcuts import render


def custom_error_404(request, exception):
    return render(request, '404.html', {})


def custom_error_403(request, exception):
    return render(request, '403.html', {})
