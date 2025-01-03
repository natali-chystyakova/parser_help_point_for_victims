from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label="Iм'я", max_length=225)
    email = forms.EmailField(label="Email")
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 60, "roes": 10}))
    capatcha = CaptchaField()
