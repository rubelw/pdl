# Simple People Data Labs Query Tool

## Prerequisites

### Python 3.6 or above must be installed

For Windows, install according to [Link](https://datatofish.com/install-python/)
For mac, install according to [Link](https://python.tutorials24x7.com/blog/how-to-install-python-3-9-on-mac)

## PIP must be installed

For Windows, install according to [Link](https://phoenixnap.com/kb/install-pip-windows)
for Mac

```bash
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

## Installation

This script will:
* Check if xcode is installed
* Homebrew is installed
* Update homebrew
* Ensure python3 and pip3 are installed
* Create a directory named .pdl in home directory
* Prompt user for people data labs api key and store in .pdl/config
* Check if virtualenv is installed
* Create virtualenv named env in ~/.pdl
* Install peopledatalabs package in virtualenv


```bash

curl --show-error --retry 5 curl https://raw.githubusercontent.com/rubelw/pdl/master/scripts/Mac/install.sh |  bash


```

## Running


Windows:

To be written


Mac:


Go to Finder -> Applications -> Utilities ->Terminal

This will open a terminal window.

Type


```bash
source ~/.pdl/env/bin/activate && pdl
```

You should receive a menu which looks like the following:


```bash
------------------------------ MENU ------------------------------
1. Phone number with 1(example: 1515986xxxx)
2. Email
3. Name,Address,City,State,Zip
4. Name, City, State
5. Name, State
6. Exit
-------------------------------------------------------------------
Enter your choice [1-5]: 
```

## Uninstalling

You can also run by entering the following into Terminal windows:

```bash
curl --show-error --retry 5 curl https://raw.githubusercontent.com/rubelw/pdl/master/scripts/Mac/uninstall.sh |  bash


```



