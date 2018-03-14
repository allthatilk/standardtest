"""A module containing tests."""
import os
from standarddoc import models


def test_HTML_file_is_created():
    """Check that an HTML file is created from an IATI XSD schema."""
    xslt_transformation = models.XSLTTransformationPage()
    xslt_transformation.transform_XSD_to_HTML()
    path = 'standarddoc/templates/iati-activities.html'
    assert os.path.isfile(path)
