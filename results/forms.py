from django import forms

class ManuallyAcceptForm(forms.Form):
    comments = forms.CharField(widget=forms.Textarea)
    operator = forms.CharField(max_length=100)
    email = forms.EmailField()


class AddingDataForm(forms.Form):
    data = forms.CharField(max_length=200)
    operator = forms.CharField(max_length=100)
    email = forms.EmailField()
      
