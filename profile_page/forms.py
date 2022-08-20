from django import forms


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

    def send_email(self) -> None:
        ...
