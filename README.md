# Automating Finance
## Introduction
This is made up of two scripts that automate the process of downloading the required data from Incorta and Microstrategy from their respective scripts. This is intended for Keysight Technologies Employees only.

## Prerequisites
- Google Chrome
- A valid Incorta and Microstrategy account
- Being connected to Keysight (Either in the office or via VPN)

## Set Up Guide
This does not need to be followed all the way if you are knowledgeable in fulfilling the requirements but is usefull if it is not working on first use.

### Incorta (Preferable but not necessary)
![Image for setting up Incorta](Images/IncortaSetUp.jpg)

To be able for the script to download the files correctly, the following files in Incorta must be in Incorta:
1. MARCOM PO REPORT - PR Number Copy
2. Marcom_invoices

If you do not have these favorited in Incorta, you can navigate to them via:
1. Marketing
2. Marcom Reports

But it is not necessary, as there is an option so the script will do it for you.

If you do decide to favorite them after navigating to them, click the star next to them to favorite them.

### Microstrategy
![Image for setting up Microstrategy](Images/MicrostrategySetUp.jpg)

Make sure that before you make the report, that the selected fields for Time, MU Hierarchy and Payment Type are as shown in the image.

## Usage
Run the executable for the data that you need. EG: incorta.exe for getting data from Incorta

You will need to enter the Login details for Incorta in the Python Shell and for Microstrategy, you have 2 minutes to login to your Keysight Account. From there, you can let the script do it's thing.

## Notes:
- if you do want to paste in the python terminal, do control + shift + v
- if you press control + c , you will force the script to end
- make sure you have no other files ending in .crdownload in you download location
