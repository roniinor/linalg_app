from django import forms

class LAForm01(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
