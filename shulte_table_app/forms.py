from django import forms

class ShulteTableForm(forms.Form):
    size = forms.IntegerField(min_value=3, max_value=10)
