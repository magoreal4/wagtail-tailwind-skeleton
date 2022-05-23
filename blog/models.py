from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

from streams import blocks

class BlogListingPage(Page):

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Titulo del blog',
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogDetailPage.objects.live().public()
        return context
    
    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
            ("full_rich_text", blocks.RichTextBlock())
        ],
        null=True,
        blank=True
    )
   
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        StreamFieldPanel("content"),
    ]

class BlogDetailPage(Page):

    blog_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Titulo del post',
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    )
    blog_content = RichTextField(
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("blog_title"),
        ImageChooserPanel('blog_image'),
        FieldPanel("blog_content"),
    ]

