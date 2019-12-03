# OpenVpn Configuration Generator

This script is a very basic python script for generating inline openvpn configuration based on a template

**This project is made for basic usage only, if you have specific needs feel free to copy it.**

**I don't plan to maintain this project**

## Installation

```bash
git clone git@github.com:thibaut-cens/OpenvpnConfigGenerator.git
pip install -r requirements.txt
```

## Usage

Check `--help` for usage informations.

This script come packed with two template files: `client.ovpn` and `server.ovpn`

Generate *server* config file:
``` bash
./ovpnCG.py --dh dh.pem --ca ca.crt --tls ta.key --cert test.crt --key test.key template/server.ovpn
```
Generate *client* config file:
``` bash
./ovpnCG.py --dh dh.pem --ca ca.crt --tls ta.key --cert test.crt --key test.key template/client.ovpn
```
