"""
Parses Raumfeld devices and writes the host address (ip and port) of the MediaRenderer to file.
"""

import requests
from xml.etree import ElementTree
from urllib.parse import urlparse

ip_address = "192.168.0.40"
base_url = "http://{}:47365/00000000-0f62-5616-0000-00000f625616/listDevices".format(ip_address)
config_file = "config.cfg"


def connect():
    port = get_port_from_media_renderer()
    write_host_to_config(ip_address, port)


def get_port_from_media_renderer():
    response = requests.get(base_url)
    if response.ok:
        tree = ElementTree.fromstring(response.content)

        for device in tree:
            if 'MediaRenderer' in device.attrib['type']:
                location = device.attrib['location']
                url = urlparse(location)
                return url.port


def write_host_to_config(ip, port):
    print('{}:{}'.format(ip, port))
    file = open(config_file, 'w')
    host = [
        get_ip_address_val_string(ip),
        get_port_val_string(port)
    ]
    file.writelines(host)
    file.close()


def get_ip_address_val_string(ip):
    name = 'ip_address'
    return '{0}="{1}"\n'.format(name, ip)


def get_port_val_string(port):
    name = 'port'
    return '{0}="{1}"\n'.format(name, port)


if __name__ == "__main__":
    connect()
