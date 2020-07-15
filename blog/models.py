from django import forms
from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from blog import blocks

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
    )
    seo_title = models.TextField(max_length=255)
    intro = RichTextField(blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('intro'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

class BlogIndexPage(RoutablePageMixin, Page):
    hero_heading = models.CharField(max_length=100, blank=False, null=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        all_posts = self.get_children().live().order_by('-first_published_at')
        pagination = Paginator(all_posts, 4)
        page = request.GET.get("page")


        try:
            blogposts = pagination.page(page)
        except PageNotAnInteger:
            blogposts = pagination.page(1)
        except EmptyPage:
            blogposts = pagination.page(pagination.num_pages)

        context['categories'] = BlogCategory.objects.all()
        context['blogposts'] = blogposts
        context['pagination'] = pagination
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_heading'),
            ImageChooserPanel('hero_image'),
        ], heading="Hero"),
        FieldPanel('intro', classname="full")
    ]

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category"""
        context = self.get_context(request)

        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            category = None
        if category is None:
            pass

        self.hero_heading = category.name
        self.seo_title = category.seo_title
        self.intro = category.intro

        all_category_posts = BlogPage.objects.filter(categories__in=[category])
        pagination = Paginator(all_category_posts, 4)
        page = request.GET.get("page")

        try:
            blogposts = pagination.page(page)
        except PageNotAnInteger:
            blogposts = pagination.page(1)
        except EmptyPage:
            blogposts = pagination.page(pagination.num_pages)

        context["blogposts"] = blogposts
        context['pagination'] = pagination
        return render(request, "blog/blog_index_page.html", context)

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogposts = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogposts'] = blogposts
        return context

class BlogPage(Page):
    hero_heading = models.CharField(max_length=100, blank=False, null=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    date = models.DateField("Post date")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    snippet = models.CharField(max_length=250)
    content = StreamField(
        [
            ("richtext_block", blocks.RichTextBlock()),
            ('two_columns', blocks.TwoColumnBlock()),
            ('imagetext_block', blocks.ImageTextBlock()),
            ('quote_block', blocks.QuoteBlock()),
            ('gallery_block', blocks.GalleryBlock()),
            ('fullwidthimage_block', blocks.FullWidthImageBlock()),
        ],
        null=True,
        blank=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('snippet'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_heading'),
            ImageChooserPanel('hero_image'),
        ], heading="Hero"),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('snippet'),
        StreamFieldPanel('content'),
    ]
