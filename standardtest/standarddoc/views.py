from django.shortcuts import render
import iati
from lxml import etree


XSL_FILE = 'iati-activities.xsl'


def create_full_activity_schema_etree():
    """Create an IATI schema with all elements and attributes from the common schema included."""
    activity_schema = iati.default.activity_schema('2.02')
    activity_schema_tree = activity_schema.flatten_includes(activity_schema._schema_base_tree)
    return activity_schema_tree

def transform_XSD_to_HTML(activity_schema_tree):
    # """Create an HTML file from an IATI XSD schema."""
    # activity_schema_full = activity_schema_tree
    # xslt = etree.parse(XSL_FILE)
    # transform = etree.XSLT(xslt)
    # html_file = transform(activity_schema_full)
    # with open('iati-activities.html', 'w') as output_file:
    #     output_file.write(html_file)
