from django import forms
from captcha.fields import CaptchaField


# class ContactForm(forms.Form):
#     name = forms.CharField(label="Iм'я", max_length=225)
#     email = forms.EmailField(label="Email")
#     content = forms.CharField(widget=forms.Textarea(attrs={"cols": 60, "rows": 10}))
#
#     captcha = CaptchaField()


class ContactForm(forms.Form):
    name = forms.CharField(label="Iм'я", max_length=225, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "cols": 60, "rows": 10}))
    captcha = CaptchaField()
