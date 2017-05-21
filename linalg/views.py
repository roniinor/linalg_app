from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import improc4
from .forms import LAForm01

def linalg_menu(request):
    return render(request, 'linalg/menu.html', {'num': get_a_number()})
    
def linalg_asciiArt(request):
    return render(request, 'linalg/ascArt.html', {'art': improc4.strPic(), 'title': "Ascii Art"})
    
#def linalg_matPage(request):
#    return render(request, 'linalg/matPage.html', {'mat': improc4.matrixFunction(), 'title': "Other Mat Fn"})

def get_a_number():
    return 14;

def linalg_matPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LAForm01(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            yname = form.cleaned_data['your_name']
            
            """
            use either redirect or render here to show the result of the form submission
            redirect will be put through a match in urls.py so parameters could be passed for processing there
            render on the same or other template can pass the from values directly as template params e.g. yname
            # redirect to a new URL:
            #return HttpResponseRedirect('/hello/')
            """
            # render another template
            return render(request, 'linalg/matPageResult.html', {'yname': yname, 'mat': improc4.matrixFunction(), 'title': "Other Mat Fn - RESULT"})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LAForm01()

    return render(request, 'linalg/matPage.html', {'form': form, 'mat': improc4.matrixFunction(), 'title': "Other Mat Fn"})
