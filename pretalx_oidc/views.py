from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretalx.common.mixins.views import PermissionRequired

from .forms import OidcSettingsForm
# from mozilla_django_oidc.auth import OIDCAuthenticationBackend
# from mozilla_django_oidc.views import OIDCLogoutView

from django.http import HttpResponse
from django.views.generic import View

class OidcSettingsView(PermissionRequired, FormView):
    permission_required = "orga.change_settings"
    template_name = "pretalx_oidc/settings.html"
    form_class = OidcSettingsForm

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
        messages.success(self.request, _("The pretalx oidc plugin settings were updated."))
        return super().form_valid(form)

class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
