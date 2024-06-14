from django import forms

class CreateProduct(forms.Form):
    description = forms.CharField(max_length=200)
    price = forms.IntegerField()
    
class FindProduct(forms.Form):
    description = forms.CharField(max_length=200, required=False)