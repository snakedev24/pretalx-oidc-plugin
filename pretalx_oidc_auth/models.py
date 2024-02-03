from django.db import models




class OidcAuthSettings(models.Model):
    event = models.OneToOneField(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="pretalx_oidc_auth_settings",
    )
    some_setting = models.CharField(max_length=10, default="A")

