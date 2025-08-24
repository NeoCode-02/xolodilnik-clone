from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class Sponsor(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    logo = models.ImageField(upload_to="sponsors", verbose_name=_("Logo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")
