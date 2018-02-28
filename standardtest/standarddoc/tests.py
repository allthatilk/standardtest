"""This is a module."""
import os
from standarddoc import views


def test_HTML_file_is_created():
    """Check that an HTML file is created from an IATI XSD schema."""
    xslt_transformation = views.XSLTTransformation()
    xslt_transformation.transform_XSD_to_HTML()
    assert os.path.isfile('standardtest/templates/iati-activities.html')
