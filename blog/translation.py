from modeltranslation import translator
from modeltranslation.translator import TranslationOptions

from blog.models import BlogCategory, BlogPost, Tag


@translator.register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@translator.register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@translator.register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)
