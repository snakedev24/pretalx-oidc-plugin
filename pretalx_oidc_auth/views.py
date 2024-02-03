from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretalx.common.mixins.views import PermissionRequired

from django.http import HttpResponse
from django.views.generic import View
from .forms import OidcAuthSettingsForm
from django.apps import AppConfig

class OidcAuthSettingsView(PermissionRequired, FormView):
    permission_required = "orga.change_settings"
    template_name = "pretalx_oidc_auth/settings.html"
    form_class = OidcAuthSettingsForm

    def get_success_url(self):
        return self.request.path

    def get_object(self):
        return self.request.event

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["event"] = self.request.event
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("The pretalx oidc auth settings were updated."))
        return super().form_valid(form)

class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")

class OIDCProviderConfig(AppConfig):
    name = 'oidc_provider.apps'
    verbose_name = _("oidc")

    class PretalxPluginMeta:
        name = _("oidc")
        author = _("the pretalx team")
        version = '1.0.0'
        visible = True
        restricted = False
        description = _("This plugin allows you to integrate OIDC.")
        category = 'INTEGRATION'

default_app_config = 'oidc_provider.apps.OIDCProviderConfig'
