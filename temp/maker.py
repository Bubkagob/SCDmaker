from lxml import objectify, etree

# ----------------------------------------------------------------------------


def create_appt(data):
    '''
    Create an appointment XML element
    '''
    appt = objectify.Element("appointement")
    appt.begin = data["begin"]
    appt.uid = data["uid"]
    appt.alarmTime = data["alarmTime"]
    appt.state = data["state"]
    appt.location = data["location"]
    appt.duration = data["duration"]
    appt.subject = data["subject"]
    return appt

# ----------------------------------------------------------------------------


def create_xml():
    '''
    Create an XML file
    '''
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
        <zAppointements>
        </zAppointements>
        '''

    root = objectify.fromstring(xml)
    root.set("reminder", "15")

    appt = create_appt(
        {
            "begin": 1181251680,
            "uid": "040000000020000E00",
            "alarmTime": 118323212,
            "state": "",
            "location": "",
            "duration": 1800,
            "subject": "Bring pizza home"
        }
    )

    root.append(appt)

    # remove lxml annotation
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    # create the xml string
    obj_xml = etree.tostring(
        root,
        pretty_print=True,
        xml_declaration=True
    )

    try:
        with open("example.xml", "wb") as xml_writer:
            xml_writer.write(obj_xml)
    except IOError:
        pass

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    create_xml()
