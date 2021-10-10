# Simple People Data Labs Query Tool

## Prerequisites


### Python 3.6 or above must be installed

For Windows, install according to [Link](https://datatofish.com/install-python/)
For mac, install according to [Link](https://python.tutorials24x7.com/blog/how-to-install-python-3-9-on-mac)

## PIP must be installed

For Windows, install according to [Link](https://phoenixnap.com/kb/install-pip-windows)
for Mac: Use homebrew to install

## Mac

Xcode and Homebrew should be installed and up-to-date

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


To run this script:

Open Windows Powershell, and copy and paste the following into the windows and press enter

Windows
-------

```bash
cd $home
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile("https://raw.githubusercontent.com/rubelw/pdl/master/scripts/Windows/install","$home/install.ps1")
./install.ps1 

```


Mac
---

Go to Finder -> Applications -> Utilities ->Terminal and paste the following line at the prompt and press enter


```bash

bash <(curl https://raw.githubusercontent.com/rubelw/pdl/master/scripts/Mac/install.sh)

```

## Running


Windows:

Open Windows Powershell window and enter the following:

```bash
cd $home/.pdl/env
.\Scripts\activate
pdl

```


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

To run this script:


Windows
-------

Open windows powershell terminal and enter the following

```bash
cd $home
rm -R -Force ./.pdl


```


Mac
---

Go to Finder -> Applications -> Utilities ->Terminal and paste the following line at the prompt and press enter

```bash
bash <(curl https://raw.githubusercontent.com/rubelw/pdl/master/scripts/Mac/uninstall.sh)

```



