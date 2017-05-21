from django.shortcuts import render
from . import improc4

def linalg_menu(request):
    return render(request, 'linalg/menu.html', {'num': get_a_number()})
    
def linalg_asciiArt(request):
    return render(request, 'linalg/ascArt.html', {'art': improc4.strPic(), 'title': "Ascii Art"})
    
def linalg_matPage(request):
    return render(request, 'linalg/matPage.html', {'mat': improc4.matrixFunction(), 'title': "Other Mat Fn"})

def get_a_number():
    return 14;
