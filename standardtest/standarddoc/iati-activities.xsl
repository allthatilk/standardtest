<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="2.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


  <xsl:template match="/">
    <xsl:apply-templates select="xsd:schema" xmlns:xsd="http://www.w3.org/2001/XMLSchema"/>
  </xsl:template>

  <xsl:output method="html"/>


  <xsl:key name="elemref" match="xsd:element" use="@name" xmlns:xsd="http://www.w3.org/2001/XMLSchema"/>
  <xsl:key name="attref" match="xsd:attribute" use="@name" xmlns:xsd="http://www.w3.org/2001/XMLSchema"/>

  <xsl:template match="xsd:schema" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsl:variable name="rootCount" select="count(xsd:element[@name='iati-activities'])"/>
    <html>
    <body>
      <xsl:apply-templates select="xsd:element[@name='iati-activities']" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsl:with-param name="rootCount" select="$rootCount"/>
      </xsl:apply-templates>
    </body>
    </html>
  </xsl:template>

  <xsl:template match="xsd:element" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsl:param name="rootCount"/>
    <div>
      <xsl:attribute name="id">
        <!-- Extract repeated values to xsl variables later -->
        <xsl:value-of select="@ref|@name"/>
      </xsl:attribute>
      <h1><xsl:value-of select="@ref|@name"/></h1>
      <h3>Definition</h3>
      <p><xsl:value-of select="key('elemref', @ref)/xsd:annotation/xsd:documentation|xsd:annotation/xsd:documentation"/></p>
      <h3>Occurance</h3>
      <p>Minimum number of times this element can occur: <xsl:value-of select="if (@minOccurs) then @minOccurs else $rootCount"/></p>
      <p>Maximum number of times this element can occur: <xsl:value-of select="if (@maxOccurs) then @maxOccurs else $rootCount"/></p>
      <h3>Attributes</h3>
      <xsl:for-each select="key('elemref', @ref)/xsd:complexType/xsd:attribute|xsd:complexType/xsd:attribute">
        <ul>
          <li><xsl:value-of select="@ref|@name"/></li>
            <ul>
              <li>
                <p>This attribute is <xsl:value-of select="if (@use) then @use else 'optional'"/></p>
                <p><xsl:value-of select="key('attref', @ref)/xsd:annotation/xsd:documentation|xsd:annotation/xsd:documentation"/></p>
              </li>
            </ul>
        </ul>
      </xsl:for-each>
      <h3>Sub-elements</h3>
      <xsl:for-each select="key('elemref', @ref)/xsd:complexType/xsd:sequence|xsd:complexType/xsd:sequence">
        <ul>
          <li><xsl:apply-templates select="xsd:element" xmlns:xsd="http://www.w3.org/2001/XMLSchema"/></li>
        </ul>
      </xsl:for-each>
    </div>
  </xsl:template>

</xsl:stylesheet>
