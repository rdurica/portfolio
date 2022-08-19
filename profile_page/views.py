from django.views import generic


# Create your views here.
class HomePage(generic.TemplateView):
    template_name: str = "profile_page/index.html"
