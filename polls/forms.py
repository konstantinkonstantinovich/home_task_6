from django import forms

from polls.models import MyPerson


class PythagoreanTheoremFrom(forms.Form):
    first_leg = forms.IntegerField(required=True)
    second_leg = forms.IntegerField(required=True)


class MyPersonModelForm(forms.ModelForm):
    class Meta:
        model = MyPerson
        fields = ["id", "email", "first_name", "last_name"]
