from django.shortcuts import render

def linalg_menu(request):
    return render(request, 'linalg/menu.html', {'num': get_a_number()})
    
    
def get_a_number():
    return 14;
