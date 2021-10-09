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

Set the API key environmental variable

Windows:

Follow example for setting an environmental variable named 'PDL_API_KEY' : [Link](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)

Mac:

```bash
export PDL_API_KEY=xxxx
```

Run the program

````bash
------------------------------ MENU ------------------------------
1. Phone number with 1(example: 1515xxxxx1)
2. Email
3. Name,Address,City,State,Zip
4. Exit
-------------------------------------------------------------------
```
