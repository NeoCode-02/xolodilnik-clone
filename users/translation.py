from modeltranslation.translator import TranslationOptions, register

from .models import Profession, User, UserFeedback


@register(Profession)
class ProfessionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(UserFeedback)
class UserFeedbackTranslationOptions(TranslationOptions):
    fields = ("message",)

