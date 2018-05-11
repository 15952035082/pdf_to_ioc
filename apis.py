import os.path

from ioc_parser.ioc_parser import IOC_Parser
from ioc_writer.toxml_api import TOXML


def pdf_to_ioc(file_path, save_path, link=None):
    parser = IOC_Parser()

    json_str = parser.parse(file_path)

    filename = GetFilename(file_path)

    with open(save_path + "\\" + filename + ".txt", "wt") as f:
        f.write(json_str)

    ioc_obj = TOXML(json_str)

    if link is not None:
        ioc_obj.add_filelink(link)

    xml = ioc_obj.write_to_xml()
    with open(save_path + "\\" + filename + ".ioc", "wt") as f:
        f.write(xml)


def txt_to_ioc(file_path, save_path, link=None):
    parser = IOC_Parser("txt")

    json_str = parser.parse(file_path)
    filename = GetFilename(file_path)

    with open(save_path + "\\" + filename + ".txt", "wt") as f:
        f.write(json_str)

    ioc_obj = TOXML(json_str)

    if link is not None:
        ioc_obj.add_filelink(link)
    xml = ioc_obj.write_to_xml()
    with open(save_path + "\\" + filename + ".ioc", "wt") as f:
        f.write(xml)


def html_to_ioc(url, save_path, add_link=True):
    parser = IOC_Parser("html")

    json_str = parser.parse(url)
    filename = GetFilename(url)

    with open(save_path + "\\" + filename + ".txt", "wt") as f:
        f.write(json_str)

    ioc_obj = TOXML(json_str)

    if add_link:
        ioc_obj.add_filelink(url)
    xml = ioc_obj.write_to_xml()
    with open(save_path + "\\" + filename + ".ioc", "wt") as f:
        f.write(xml)


def GetFilename(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    (shotname, extension) = os.path.splitext(tempfilename)
    return shotname


txt_to_ioc("D:\\sourcefile\\b.txt", "D:\\iocfile",
           "https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections/blob/master/2010/Aurora_HBGARY_DRAFT.pdf")
