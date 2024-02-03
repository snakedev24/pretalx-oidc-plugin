
from django.urls import re_path, path, include
from pretalx.event.models.event import SLUG_CHARS

from .views import OidcSettingsView, HelloWorldView

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_CHARS})/settings/p/pretalx_oidc/$",
        OidcSettingsView.as_view(),
        name="settings",
    ),
    re_path(
        rf"^orga/event/(?P<event>{SLUG_CHARS})/settings/p/hello_world/$",
        HelloWorldView.as_view(),
        name="hello_world",
    ),
    # path("oidc/", include("mozilla_django_oidc.urls")),
]

