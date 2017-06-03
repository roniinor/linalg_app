from django import forms

class LAForm01(forms.Form):

    def __init__(self, *args, **kwargs):
        if 'qal' in kwargs:
            qal = kwargs.pop('qal')
            super(LAForm01, self).__init__(*args, **kwargs)
            qanum = 0
            for qa in qal:
                #qal is the question answer list which alternates question, answer so 
                # %2 is used first (if) to get question then (else) to get answer 
                qnum = qanum // 2
                if qanum % 2 == 0:
                    self.fields['answer-' + str(qnum)] = forms.CharField(label=qa, max_length=30, widget=forms.NumberInput)
                    self.fields['hiddenq-' + str(qnum)] = forms.CharField(initial=qa, widget=forms.HiddenInput)
                else:
                    self.fields['hiddena-' + str(qnum)] = forms.CharField(initial=qa, widget=forms.HiddenInput)
                qanum += 1
        else:
            super(LAForm01, self).__init__(*args, **kwargs)

    def q_marks(self, n):
        qm = []
        for i in range(n):
            if self.cleaned_data['answer-' + str(i)] == self.cleaned_data['hiddena-' + str(i)]:
                qm.append("-CORRECT-")
            else:
                qm.append("--WRONG--")
        return qm



"""
solution for multiple/list of fields
 from https://jacobian.org/writing/dynamic-form-generation/
 also see https://stackoverflow.com/questions/17159567/how-to-create-a-list-of-fields-in-django-forms

forms documentation
 working with - https://docs.djangoproject.com/en/1.10/topics/forms/
 reference - https://docs.djangoproject.com/en/1.10/ref/forms/
 field widgets - https://docs.djangoproject.com/en/1.10/ref/forms/widgets/


    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for i, question in enumerate(extra):
            self.fields['custom_%s' % i] = forms.CharField(label=question)
"""
