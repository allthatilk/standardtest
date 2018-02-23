# from django.test import TestCase
# import pytest
# from .activity_schema_full import FULL_ACTIVITY_SCHEMA_STRING
from standarddoc import views


XSL_FILE = 'iati-activities.xsl'


def test_etree_to_HTML_transformation():
    """Check that an HTML file is created from an IATI XSD schema."""
    activity_schema_tree = create_full_activity_schema_etree()
    transform_XSD_to_HTML(activity_schema_tree)
    assert os.path.is_file('iati-activities.html')
