from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePageFeaturedPosts(Orderable):
    page = ParentalKey("home.HomePage", related_name="featured_posts")
    featured_post = models.ForeignKey(
        'wagtailcore.Page', on_delete=models.CASCADE, related_name='+'
    )
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        PageChooserPanel('featured_post'),
        ImageChooserPanel('featured_image'),
    ]

class HomePage(Page):
    max_count = 1

    hero_heading = models.CharField(max_length=100, blank=False, null=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    intro = RichTextField(blank=True)
    featured_section = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_heading'),
            ImageChooserPanel('hero_image'),
        ], heading="Hero"),
        FieldPanel('intro', classname="full"),
        MultiFieldPanel([
            FieldPanel('featured_section'),
            InlinePanel('featured_posts', max_num=6, label="Post"),
        ], heading="Featured"),
    ]
