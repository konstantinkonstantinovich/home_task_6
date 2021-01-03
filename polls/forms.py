from django import forms


class PythagoreanTheoremFrom(forms.Form):
    first_leg = forms.IntegerField(required=True)
    second_leg = forms.IntegerField(required=True)
