import xmlschema


scl_schema = xmlschema.XMLSchema("SCL.xsd")

print(scl_schema.validate("B20.icd"))

