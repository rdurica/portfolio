from django.views import generic


# Create your views here.
class Gallery(generic.TemplateView):
    template_name: str = "gallery/gallery.html"
