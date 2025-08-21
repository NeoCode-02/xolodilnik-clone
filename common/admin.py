from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from common.models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(TranslationAdmin):
    list_display = (
        "id",
        "name",
        "logo",
    )
    search_fields = ("name",)
