### Athena project

The Greek goddess statue with a heart in her chest that pumps after tags/commets in Instagram

Using **pyInstagram** for getting data.
***

### Installation  
```bash
1. git clone https://github.com/olegyurchik/pyInstagram.git
2. cd pyInstagram
3. pip3 install .
```
***

### Raspberry Pi 4
Download Raspbian Buster lite from [here](https://www.raspberrypi.org/downloads/raspbian/). Burn the Raspbian image to the SD card. To use Raspberry without display you need enable ssh to allow remote login. You can do that placing an empty file named ssh (no extension) in the root of the boot disk.
Then you neen to add your WiFi network info. Create a file in the root of boot called: **wpa_supplicant.conf**. Then paste the following into it (with your country code, NETWORK-NAME and NETWORK-PASSWORD):
```
country=RU
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```
Then you'll be able to connect with Raspberry via ssh.

Install GPIO library for python
```bash
1. sudo apt-get update
2. sudo apt-get install python3-rpi.gpio
```
Install tmux
```bash
1. sudo apt-get update
2. sudo apt-get install tmux
```
