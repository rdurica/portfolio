from captcha.fields import CaptchaField
from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "name@example.com",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 8})
    )
    captcha = CaptchaField()

    def send_email(self) -> None:
        html_body = render_to_string(
            "profile_page/email/contact.html",
            {"data": self.cleaned_data},
        )

        message = EmailMessage("New message", html_body, to=["r.durica@gmail.com"])
        message.content_subtype = "html"
        message.send()
