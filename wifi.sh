#!/bin/bash

echo '' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo 'network={' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo '	ssid="'$1'"' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo '	psk="'$2'"' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo '}' >> /etc/wpa_supplicant/wpa_supplicant.conf
