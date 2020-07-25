from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core.models import Page, Orderable
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from blog import blocks

class DefaultPage(Page):
    hero_heading = models.CharField(max_length=100, blank=False, null=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content = StreamField(
        [
            ("richtext_block", blocks.RichTextBlock()),
            ('two_columns', blocks.TwoColumnBlock()),
            ('imagetext_block', blocks.ImageTextBlock()),
            ('quote_block', blocks.QuoteBlock()),
            ('gallery_block', blocks.GalleryBlock()),
            ('fullwidthimage_block', blocks.FullWidthImageBlock()),
            ('cta_block', blocks.CTABlock()),
            ('floatingcards_block', blocks.FloatingCardsBlock()),
            ('faq_block', blocks.FAQBlock()),
            ('testimonials_block', blocks.TestimonialsBlock()),
        ],
        null=True,
        blank=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_heading'),
            ImageChooserPanel('hero_image'),
        ], heading="Hero"),
        StreamFieldPanel('content'),
    ]
