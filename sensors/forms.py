from django import forms


class Feedback(forms.Form):
    phone = forms.CharField()
    name = forms.CharField()