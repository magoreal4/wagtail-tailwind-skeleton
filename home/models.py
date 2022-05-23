from django.db import models

from wagtail.core.models import Page
from wagtailseo.models import SeoMixin

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(SeoMixin, Page):
    promote_panels = SeoMixin.seo_panels

    banner_title = models.CharField(
        "titulo H1",
        max_length=30,
        blank=False,
        null=True,
        default='Paint Ball Park - Santa Cruz'
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
    ]

    # class Meta:
    #     verbose_name = "Pagina Inicial"

class HomePageBanner(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='carousel_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=30, blank=False, null=True)
    description = models.CharField(blank=True, max_length=100)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]