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
        """
        various choices here. Populating with post data or just use the POST data without a form
        e.g. in this case if rendering another page for feedback which does not need to be on a
        form at all then just extract data from request.POST rather than creating a form at all
        and pass this data to render the required template e.g with something like
            #return render(request, 'linalg/matPageResult.html', {'qa': qa, 'mat': improc4.matrixFunction(), 'title': "Other Mat Fn - RESULT"})
        """
        qaList = []
        for i in range(5):
            qaList.append(request.POST['hiddenq-' + str(i)])
            qaList.append(request.POST['hiddena-' + str(i)])
        
        # **** HERE **** append CORRECT/WRONG to qalist somehow, better now to use some form of tuples
        # then in form template use some sort of CSS attribute to say colour correct and wrong answers

        form = LAForm01(request.POST, qal=qaList)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # check if answers are correct and display message by inputs

            """
            use either redirect or render here to show the result of the form submission
            redirect will be put through a match in urls.py so parameters could be passed for processing there
            render on the same or other template can pass the from values directly as template params e.g. yname
            # redirect to a new URL:
            #return HttpResponseRedirect('/hello/')
            """
            # render another template
            return render(request, 'linalg/matPage.html', {'form': form, 'mat': improc4.matrixFunction(), 'marks': form.q_marks(5), 'title': "RESUBMIT Mat Fn"})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        qaList = improc4.twoDigitMultiplyQAList(5)
        form = LAForm01(qal=qaList)

    return render(request, 'linalg/matPage.html', {'form': form, 'mat': improc4.matrixFunction(), 'title': "Other Mat Fn"})
