from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
 
class HomePage(Page):
    # Sample Section
    image_link = models.CharField(
        blank=True,
        verbose_name="Image Link",
        max_length=255,
        help_text="Link for Image to embed",
    )
    text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    yt_link = models.CharField(
        blank=True,
        verbose_name="YouTube Video Link",
        max_length=255,
        help_text="Link for YouTube Video to embed",
    )
    pdf_link = models.CharField(
        blank=True,
        verbose_name="PDF Link",
        max_length=255,
        help_text="Link for .pdf file to embed",
    )
    link = models.CharField(
        blank=True,
        verbose_name="Link",
        max_length=255,
        help_text="Link",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image_link"),
                FieldPanel("text"),
                FieldPanel("yt_link"),
                FieldPanel("pdf_link"),
                FieldPanel("link"),
            ],
            heading="Sample section",
        ),
        FieldPanel('body'),
    ]