"""StreamFields live in here"""

from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "blocks/richtext_block.html"
        icon = "edit"
        label = "Rich Text"

class TwoColumnBlock(blocks.StructBlock):

    left_column = RichTextBlock(icon='arrow-right', label='Left column content')
    right_column = RichTextBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

class ImageTextBlock(blocks.StructBlock):

    left_column = ImageChooserBlock(icon='arrow-right', label='Left column image')
    right_column = RichTextBlock(icon='arrow-right', label='Right column text')

    class Meta:
        template = 'blocks/imagetext_block.html'
        icon = 'image'
        label = 'Image & Text Columns'

class QuoteBlock(blocks.StructBlock):

    quote = blocks.TextBlock(icon="openquote", label="Quote")
    attribution = blocks.CharBlock(icon="user", label="Attribution")

    class Meta:
        template = "blocks/quote_block.html"
        icon = "openquote"
        label = "Blockquote"

class GalleryBlock(blocks.StreamBlock):
    image = ImageChooserBlock(icon='image', label='Gallery image')

    class Meta:
        template = "blocks/gallery_block.html"
        icon = "image"
        label = "Image Gallery"

class FullWidthImageBlock(ImageChooserBlock):

    class Meta:
        template = "blocks/fullwidthimage_block.html"
        icon = "image"
        label = "Full-Width Image"
