from django.shortcuts import render
from . import improc3

def linalg_menu(request):
    return render(request, 'linalg/menu.html', {'num': get_a_number()})
    
def linalg_asciiArt(request):
    return render(request, 'linalg/ascArt.html', {'art': improc3.strPic()})
    

def get_a_number():
    return 14;
