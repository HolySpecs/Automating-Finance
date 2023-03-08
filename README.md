# Automating Finance

## Introduction
This is made up of two scripts that automate the process of downloading the required data from Incorta and Microstrategy from their respective scripts. This is intended for Keysight Technologies Employees only.

## Requirements
1. Python 3.8 or higher (3.10.10 was used)
2. Selenium 4.8
3. webdriver_manager
4. A valid Incorta and Microstrategy account

## Set Up Guide
This does not need to be followed all the way if you are knowledgeable in fulfilling the requirements but is usefull if it is not working on first use.

### Incorta
To be able for the script to download the files correctly, the following files in Incorta must be favorited:
1. MARCOM PO REPORT - PR Number Copy
2. Marcom_invoices

### Microstrategy


Steps to follow before running script:
- Download Python (anything above 3.8 is ok)
	- Python is the programming language that's used .
	- Go to the link https://www.microsoft.com/store/productId/9NRWMJP3717K in your browser
	- Follow the instructions to download Python (the link downloads Python 3.11)
	- Close the window when Python is done downloading
- Open PowerShell (we use this to download the tools)
	- Right click the Windows Icon
	- Click Windows PowerShell
- Downloading the tools
	- Selenium is a library that allows Python to automate browser tasks
		- Copy (control + c) the stuff in quotes "pip install selenium"
		- Paste (control + shift + v) in Windows PowerShell
		- Press Enter and wait for it to complete (when you can enter text)
	- webdriver_manager allows us run Chrome specifically
		- Copy (control + c) the stuff in quotes "pip install webdriver-manager"
		- Paste (control + shift + v) in Windows PowerShell
		- Press Enter and wait for it to complete (when you can enter text)
- You can now close Windows PowerShell and run incorta.py

How to use incorta.py:
-run python script (recommend open with and find python)
-enter the details when asked
-let the script do it's thing
-check to make sure that it downloaded the files.

Notes for incorta.py:
- Make sure that you have an account for Incorta
- These must be in your favourites in Incorta:
    - MARCOM PO REPORT - PR Number Copy
    - Marcom_invoices
- To mark things as a favourite, click the star next to a file
- if you do want to paste in the python terminal, do control + shift + v
- if you press control + c , you will force the script to end
- make sure you have no other files ending in .crdownload in you download location
