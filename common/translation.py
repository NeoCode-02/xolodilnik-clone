from modeltranslation.translator import TranslationOptions, register

from .models import Sponsor


@register(Sponsor)
class SponsorTranslationOptions(TranslationOptions):
    fields = ("name",)
