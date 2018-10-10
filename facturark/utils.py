import os
from datetime import date, datetime
from lxml.etree import parse, XMLSchema, SubElement


def parse_xsd(path):
    directory = os.path.dirname(os.path.realpath(__file__))
    xsd_doc = parse(os.path.join(directory, path))
    return XMLSchema(xsd_doc)


def make_child(parent, tag, text=None, attributes=None,
               required=True, empty=False):
    child = None
    if empty and (text or attributes):
        raise ValueError("The <{}> tag should be empty but text "
                         "or attributes were given.".format(tag))

    if (required and not empty) and not (text or attributes):
        raise ValueError("The <{}> tag is required".format(tag))

    if empty:
        child = SubElement(parent, tag)
    elif text or attributes:
        child = SubElement(parent, tag, attributes)
        if text:
            child.text = text

    return child


def json_serialize(object_):
    """JSON serializer for objects not serializable"""
    if isinstance(object_, (datetime, date)):
        return object_.isoformat()
    raise TypeError ("Type %s not serializable" % type(object_))
