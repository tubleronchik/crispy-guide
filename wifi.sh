#!/bin/bash

np=$(grep \" /etc/wpa_supplicant/wpa_supplicant.conf | awk -F"\"" '{print $2}')
name=$(echo $np | awk '{print $1}')
pass=$(echo $np | awk '{print $2}')
sed -i "s/$name/$1/g" /etc/wpa_supplicant/wpa_supplicant.conf
sed -i "s/$pass/$2/g" /etc/wpa_supplicant/wpa_supplicant.conf

