from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "pretalx_oidc"
    verbose_name = "pretalx oidc plugin"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx oidc plugin")
        author = "Your name"
        description = gettext_lazy("pretalx plugin for oidc auth")
        visible = True
        version = __version__
        category = "FEATURE"

    def ready(self):
        from . import signals  # NOQA
