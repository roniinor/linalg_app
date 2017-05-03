from django.shortcuts import render

def linalg_menu(request):
    return render(request, 'linalg/menu.html', {})
