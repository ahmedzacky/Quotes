from django.shortcuts import render


def err_page(request, message):
    return render(request, 'error_page.html', {message})
