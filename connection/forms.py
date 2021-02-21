from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'size': '40',
                                                            'class': 'form-control'}))  # noqa: E501
    from_email = forms.EmailField(widget=forms.
                                  TextInput(attrs={'size': '40',
                                                   'class': 'form-control'}))
    message = forms.CharField(widget=forms.
                              Textarea(attrs={'class': 'form-control'}))
