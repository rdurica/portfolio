from django import urls
from django.urls import include, path

from gallery.views import Gallery

app_name: str = "gallery"
urlpatterns = [
    path("", Gallery.as_view(), name="gallery"),
]
