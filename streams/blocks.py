from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks

class CardBlock(blocks.StructBlock):

    title = blocks.CharBlock(requiered=True, help_text='Add title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(requiered=True)),
                ("title", blocks.CharBlock(requiered=True, max_length=40)),
                ("text", blocks.TextBlock(requiered=True, max_length=80)),
                ("button_card", blocks.PageChooserBlock(requiered=False)),
                ("button_url", blocks.URLBlock(requiered=False)),
            ]
        ),
    )

    class Meta:
        tempate = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"

class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full Rich Text Block"
