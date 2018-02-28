from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from standarddoc import views


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class StandardPage(Page):
    xslt_transformation = views.XSLTTransformation()
    autogen = xslt_transformation.transform_XSD_to_HTML()
    example_code = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('example_code', classname="full"),
    ]
