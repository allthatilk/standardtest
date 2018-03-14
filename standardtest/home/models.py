from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from standarddoc import models


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class StandardPage(Page):
    xslt_transformation = models.XSLTTransformationPage()
    autogen = xslt_transformation.transform_XSD_to_HTML()
    example_code = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('example_code', classname="full"),
    ]
