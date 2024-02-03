from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretalx_oidc_auth"
    verbose_name = "pretalx oidc auth"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx oidc auth")
        author = "Your name"
        description = gettext_lazy("pretalx plugin for OIDC authentication")
        visible = True
        version = __version__
        category = "FEATURE"

    def ready(self):
        from . import signals  # NOQA
