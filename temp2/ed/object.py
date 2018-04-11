from lxml import objectify, etree

def objectify_parse_with_schema(schemaname, infilename):
    schema = etree.XMLSchema(file=schemaname)
    parser = objectify.makeparser(schema=schema)
    doctree = objectify.parse(infilename, parser=parser)
    root = doctree.getroot()
    return doctree, root


doctree, root = objectify_parse_with_schema("SCL.xsd", "B20.icd")
FILE = open("output.xml", "w")
FILE.writelines(etree.tostring(root))
FILE.close()
# output = etree.tostring(doctree, pretty_print=True)
