from django.views import generic

from gallery.models import Item


# Create your views here.
class Gallery(generic.ListView):
    template_name: str = "gallery/gallery.html"
    context_object_name: str | None = "gallery_items"

    def get_queryset(self) -> list[Item]:
        return Item.objects.filter(is_enabled=True)
