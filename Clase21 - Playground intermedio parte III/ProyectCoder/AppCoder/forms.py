from django import forms

class DeliveredForm(forms.Form):
    name = forms.CharField(max_length=30)
    deadline = forms.DateField()
    delivered = forms.BooleanField()