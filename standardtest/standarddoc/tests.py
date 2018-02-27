"""This is a module."""
import os
from standarddoc import views


# XSL_FILE = 'iati_activities.xsl'


def test_HTML_file_is_created():
    """Check that an HTML file is created from an IATI XSD schema."""
    activity_schema_tree = views.create_full_activity_schema_etree()
    views.transform_XSD_to_HTML(activity_schema_tree)
    assert os.path.isfile('standarddoc/templates/standarddoc/iati-activities.html')
