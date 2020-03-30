#!/bin/bash

directory_name=$(dirname "$0")
source $directory_name/config.cfg

curl -H 'SOAPACTION: "urn:schemas-upnp-org:service:RenderingControl:1#ChangeVolume"' -H 'Accept-Language: en' -H 'User-Agent: RaumfeldControl/4.13 RaumfeldProtocol/399 Build/11063 Android/10' -H 'Content-Type: application/xml; charset=utf-8' -H 'Host: '$host --data-binary "<?xml version='1.0' ?><s:Envelope s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:u=\"urn:schemas-upnp-org:service:RenderingControl:1\"><s:Body><u:ChangeVolume><Amount>"$1"</Amount></u:ChangeVolume></s:Body></s:Envelope>" --compressed 'http://'$host'/RenderingControl/ctrl'