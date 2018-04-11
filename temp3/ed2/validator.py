from lxml import etree
from io import StringIO

def validate(xml_path:str, xsd_path:str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    log = xmlschema.error_log
    error = log.last_error

    return (result, error)


f = StringIO('''\
             <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
             <xs:element name="students">
             <xs:complexType>
             <xs:sequence>
             <xs:element name = "student">
             <xs:complexType>
             <xs:sequence>
             <xs:element name = "name" type = "xs:string"/>
             <xs:element name = "surname" type = "xs:string"/>
             <xs:element name = "fathername" type = "xs:string"/>
             <xs:element name = "university" type = "xs:string"/>
             </xs:sequence>
             <xs:attribute name="id" type="xs:int"/>
             </xs:complexType>
             </xs:element>
             </xs:sequence>
             </xs:complexType>
             </xs:element>
             </xs:schema>'''
             )

valid = StringIO('''\
                 <students
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="students.xsd"
                 >
                 <student id = "1">
                 <name>Elizabeth</name>
                 <surname>Karpova</surname>
                 <fathername>Konstantinova</fathername>
                 <university>SpbGU</university>
                 </student>
                 </students>'''
                 )

print(validate("B20.icd", "SCL.xsd"))
