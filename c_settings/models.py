

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, HelpPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtailsvg.models import Svg
from wagtailsvg.edit_handlers import SvgChooserPanel
from .fields import MonospaceField


@register_setting(icon='cr-desktop')
class Logo(BaseSetting):
    
    logo = models.ForeignKey(
        Svg,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Logo SVG'),
        help_text=_("Archivo SVG -- Ejemplo.... <svg class='w-8 h-8' xmlns='http://www.w3.org/2000/svg'    version='1.1' viewBox='0 0 350 350'>   <g transform='translate(-258.272 -38.53)'>  <path fill='currentColor' d='m342.425 ...' />    </g> </svg>")
    )

    favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='favicon',
        verbose_name=_('Favicon'),
        help_text=_("Archivo recomendado 180x180")
    )

    panels = [
        MultiFieldPanel([
            SvgChooserPanel('logo'),
            ImageChooserPanel('favicon'),
        ], heading="Logos"),
    ]


@register_setting
class Social(BaseSetting):

    facebook = models.URLField(
        blank=True, null=True, help_text="facebook page")
    instagram = models.URLField(blank=True, null=True, help_text="instagram")
    youtube = models.URLField(blank=True, null=True,
                              help_text="youtube channel")
    whatsapp = models.CharField(
        blank=True, null=True, help_text="Telefono whtasapp +591xxxxxxxx", max_length=12)

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("youtube"),
            FieldPanel("whatsapp"),
        ], heading="Social Media Settings"),
    ]

@register_setting(icon='cog')
class GeneralSettings(BaseSetting):
    """
    Various site-wide settings. A good place to put
    one-off settings that don't belong anywhere else.
    """

    from_email_address = models.CharField(

        blank=True,
        max_length=255,
        verbose_name=_('From email address'),
        help_text=_('The default email address this site appears to send from. For example: "sender@example.com" or "Sender Name <sender@example.com>" (without quotes)'),  # noqa
    )
    search_num_results = models.PositiveIntegerField(
        default=10,
        verbose_name=_('Number of results per page'),
    )
    external_new_tab = models.BooleanField(
        default=False,
        verbose_name=_('Open all external links in new tab')
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('from_email_address'),
            ],
            _('Email')
        ),
        MultiFieldPanel(
            [
                FieldPanel('search_num_results'),
            ],
            _('Search Settings')
        ),
        MultiFieldPanel(
            [
                FieldPanel('external_new_tab'),
            ],
            _('Links')
        ),
    ]

    class Meta:
        verbose_name = _('General')

@register_setting(icon='cog')
class AnalyticsSettings(BaseSetting):
    """
    Tracking and Google Analytics.
    """
    class Meta:
        verbose_name = _('Tracking')

    ga_tracking_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('UA Tracking ID'),
        help_text=_('Your Google "Universal Analytics" tracking ID (begins with "UA-")'),
    )
    ga_g_tracking_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('G Tracking ID'),
        help_text=_('Your Google Analytics 4 tracking ID (begins with "G-")'),
    )
    ga_track_button_clicks = models.BooleanField(
        default=False,
        verbose_name=_('Track button clicks'),
        help_text=_('Track all button clicks using Google Analytics event tracking. Event tracking details can be specified in each button’s advanced settings options.'),  # noqa
    )
    gtm_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('Google Tag Manager ID'),
        help_text=_('Begins with "GTM-"'),
    )
    head_scripts = MonospaceField(
        blank=True,
        null=True,
        verbose_name=_('<head> tracking scripts'),
        help_text=_('Add tracking scripts between the <head> tags.'),
    )
    body_scripts = MonospaceField(
        blank=True,
        null=True,
        verbose_name=_('<body> tracking scripts'),
        help_text=_('Add tracking scripts toward closing <body> tag.'),
    )

    panels = [
        HelpPanel(
            heading=_('Know your tracking'),
            content=_(
                '<h3><b>Which tracking IDs do I need?</b></h3>'
                '<p>Before adding tracking to your site, '
                '<a href="https://docs.coderedcorp.com/wagtail-crx/how_to/add_tracking_scripts.html" '  # noqa
                'target="_blank">read about the difference between UA, G, GTM, '
                'and other tracking IDs</a>.</p>'
            ),
        ),
        MultiFieldPanel(
            [
                FieldPanel('ga_tracking_id'),
                FieldPanel('ga_g_tracking_id'),
                FieldPanel('ga_track_button_clicks'),
            ],
            heading=_('Google Analytics'),
        ),
        MultiFieldPanel(
            [
                FieldPanel('gtm_id'),
            ],
            heading=_('Google Tag Manager'),
        ),
        MultiFieldPanel(
            [
                FieldPanel('head_scripts'),
                FieldPanel('body_scripts'),
            ],
            heading=_('Other Tracking Scripts')
        )
    ]