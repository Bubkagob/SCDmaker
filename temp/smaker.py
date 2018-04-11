from lxml import etree
# from copy import copy
SCHEMA_SPACE = "{http://www.w3.org/2001/XMLSchema}"


class MySchema:

    def __init__(self, schemafile):
        self.root = etree.parse(schemafile)

    def findall(self, path):
        return self.root.findall(path.replace("xs:", SCHEMA_SPACE))

    def find(self, path):
        return self.root.find(path.replace("xs:", SCHEMA_SPACE))

    def names_of(self, nodes):
        return [node.get("name") for node in nodes]

    def get_types(self, t_name):
        return self.names_of(self.findall(t_name))

    def get_simpletypes(self):
        return self.get_types("xs:simpleType")

    def get_complextypes(self):
        return self.get_types("xs:complexType")

    def get_elements_of_attribute(self, attribute):
        return self.names_of(
            self.findall(
                ".//xs:element/xs:complexType/xs:" + attribute + "/../.."))

    def get_element_attributes(self, name):

        node = self.find(".//xs:element[@name='" + name + "']")
        if node is None:
            node = self.find(".//xs:complexType[@name='" + name + "']")

        if node is None:
            return None
        else:
            return node.attrib


if __name__ == "__main__":
    with open("SCL.xsd") as f:
        schema = MySchema(f)

        print(schema.get_simpletypes())
        print(schema.get_complextypes())
        print(schema.get_elements_of_attribute("xpath"))
