
from django.urls import re_path
from pretalx.event.models.event import SLUG_CHARS

from .views import OidcAuthSettings, HelloWorldView

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_CHARS})/settings/p/pretalx_oidc_auth/$",
        OidcAuthSettings.as_view(),
        name="settings",
    ),
    re_path(
        rf"^orga/event/(?P<event>{SLUG_CHARS})/settings/p/hello_world/$",
        HelloWorldView.as_view(),
        name="hello_world",
    ),
]
