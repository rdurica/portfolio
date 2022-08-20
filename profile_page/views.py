from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from profile_page.forms import ContactForm


# Create your views here.
class HomePage(generic.FormView):
    template_name: str = "profile_page/index.html"
    form_class = ContactForm

    def get_success_url(self) -> str:
        return reverse("profile_page:home")

    def form_valid(self, form: ContactForm) -> HttpResponse:
        form.send_email()
        messages.success(
            request=self.request,
            message="Thank you for your message. I will contact you as soon as possible",
        )
        return super().form_valid(form)
