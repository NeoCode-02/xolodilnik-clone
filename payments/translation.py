from modeltranslation.translator import TranslationOptions, register
from payments.models import Discount, Promocode


@register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ("name", "description")


@register(Promocode)
class PromocodeTranslationOptions(TranslationOptions):
    fields = ("description",)


