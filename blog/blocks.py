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

    left_column = RichTextBlock(icon='arrow-left', label='Left column content')
    right_column = RichTextBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

class ImageTextBlock(blocks.StructBlock):

    left_column = ImageChooserBlock(icon='arrow-left', label='Left column image')
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

class CTABlock(blocks.StructBlock):

    cta_text = RichTextBlock(icon='edit', label='CTA block copy')
    cta_button = blocks.TextBlock(icon='pick', label='CTA button text')
    cta_link = blocks.PageChooserBlock(icon='site', label='Link')

    class Meta:
        template = 'blocks/cta_block.html'
        icon = 'pick'
        label = 'Full-Width CTA'

class FloatingCardsBlock(blocks.StreamBlock):

    float_card_left = RichTextBlock(icon='arrow-left', label='Float card left')
    float_card_right = RichTextBlock(icon='arrow-right', label='Float card right')

    class Meta:
        template = "blocks/floatingcards_block.html"
        icon = "list-ul"
        label = "Floating Cards"

class FAQBlock(blocks.StreamBlock):

    faq = blocks.StructBlock([
        ('question', blocks.TextBlock(icon='help', label='FAQ Question')),
        ('answer', RichTextBlock(icon='edit', label='FAQ Answer')),
    ], icon='help')

    class Meta:
        template = "blocks/faq_block.html"
        icon = "help"
        label = "FAQ Dropdown"

class TestimonialsBlock(blocks.StreamBlock):

    testimonial = blocks.StructBlock([
        ('testimonial', blocks.TextBlock(icon='help', label='Testimonial')),
        ('client', RichTextBlock(icon='edit', label='Client')),
    ], icon='help')

    class Meta:
        template = "blocks/testimonials_block.html"
        icon = "openquote"
        label = "Testimonials Slider"
