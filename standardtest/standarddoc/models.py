from django.db import models
import iati
import os
from lxml import etree
from standardtest.settings import base


class XSLTTransformationPage(object):

    XSL_FILE = os.path.join(base.BASE_DIR, 'standarddoc', 'static', 'iati_activities.xsl')

    def create_full_activity_schema_etree(self):
        """Create an IATI schema with arelevant content from the common schema included."""
        activity_schema = iati.default.activity_schema('2.02')
        activity_schema_tree = activity_schema.flatten_includes(activity_schema._schema_base_tree)
        return activity_schema_tree

    def parse_XSL_template(self):
        """Turn XSL document into an XSLT object."""
        return etree.parse(self.XSL_FILE)

    def transform_XSD_to_HTML(self):
        """Create an HTML file from an IATI XSD schema."""
        activity_schema_full = self.create_full_activity_schema_etree()
        transform = etree.XSLT(self.parse_XSL_template())
        html_tree = transform(activity_schema_full)
        # The write method is used as the write_output method that uses the xsl:output tag doesn't provide correct indenting or DOCTYPE format.
        html_tree.write(
            os.path.join(base.BASE_DIR, 'standarddoc', 'templates', 'iati-activities.html'),
            doctype='<!DOCTYPE html>',
            encoding='UTF-8',
            pretty_print=True
        )
        # return(html_tree)
