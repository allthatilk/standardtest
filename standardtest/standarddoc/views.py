from django.shortcuts import render
import iati
from lxml import etree


XSL_FILE = 'standarddoc/iati_activities.xsl'


def create_full_activity_schema_etree():
    """Create an IATI schema with all elements and attributes from the common schema included."""
    activity_schema = iati.default.activity_schema('2.02')
    activity_schema_tree = activity_schema.flatten_includes(activity_schema._schema_base_tree)
    return activity_schema_tree


def parse_XSL_template():
    """Turn XSL document into an XSLT object."""


def transform_XSD_to_HTML(activity_schema_tree):
    """Create an HTML file from an IATI XSD schema."""
    activity_schema_full = activity_schema_tree
    xslt = etree.parse(XSL_FILE)
    transform = etree.XSLT(xslt)
    html_tree = transform(activity_schema_full)
    # The write method is used as the write_output method that uses the xsl:output tag doesn't provide correct indenting or DOCTYPE format.
    html_tree.write('standarddoc/templates/standarddoc/iati-activities.html', doctype='<!DOCTYPE html>', encoding='UTF-8', pretty_print=True)


def iati_activities(request):
    """Render the index page."""
    return render(request, 'standarddoc/iati-activities.html', {})
