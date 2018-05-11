import json
from ioc_writer.ioc_api import IOC, make_indicatoritem_node, get_top_level_indicator_node


class TOXML(object):
    """
    Class for Converting json to OpenIOC file.
    Currently only supports 'OR' logic
    Currently only supported 'type' (ip/ipv4,dns,sha1,email,uri)

    """

    def __init__(self, source):
        self.ioc_file = IOC()  # Generates all parts of an IOC, but without any definition
        self.ioc_file.make_ioc()
        _list = json.loads(source)  # Turn json_str to list
        for dic in _list:  # Generate corresponding xml field based on input dic
            _type = dic["type"]
            content = dic["content"]
            node = self.make_node(_type, content)
            get_top_level_indicator_node(self.ioc_file.root).append(node)

    """
        Return xml that conforms to the OpenIOC standard format 
    """

    def write_to_xml(self):
        return self.ioc_file.write_ioc_to_string()

    """
        Generate different node according to different types                        
    """

    def make_node(self, content_type, content):
        if content_type.lower() == 'ip' or content_type.lower() == 'ipv4':
            return self.make_node_ip(content_type, content)

        if content_type.lower() == 'dns':
            return self.make_node_dns(content)

        if content_type.lower() == 'sha1':
            return self.make_node_filename(content_type, content)

        if content_type.lower() == 'email':
            return self.make_node_email(content)

        if content_type.lower() == 'uri' or content_type.lower() == 'url':
            return self.make_node_uri(content)
        raise Exception("Unsupported type,Currently only supported 'type' (ip/ipv4,dns,sha1,email,uri)")

    """




    """

    @staticmethod
    def make_node_ip(content_type, content):
        return make_indicatoritem_node("is", "PortItem", "PortItem/remoteIP", content_type, content)

    @staticmethod
    def make_node_dns(content):
        return make_indicatoritem_node("is", "DnsEntryItem", "DnsEntryItem/Host", "string", content)

    @staticmethod
    def make_node_uri(content):
        return make_indicatoritem_node("is", "Network", "Network/URI", "string", content)

    @staticmethod
    def make_node_filename(content_type, content):
        return make_indicatoritem_node("is", "FileItem", "FileItem/Sha1sum", content_type, content)

    @staticmethod
    def make_node_email(content):
        return make_indicatoritem_node("is", "Email", "Email/From", "string", content)

    def add_filelink(self, link, href=None):

        self.ioc_file.add_link("link", link, href)
