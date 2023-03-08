import os
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

PATH_TO_DOWNLOADS = str(Path.home() / "Downloads")

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.get("https://bi-prod.is.keysight.com/MicroStrategy/servlet/mstrWeb")
#wait for the user to enter their details
WebDriverWait(driver, 120).until(EC.url_to_be("https://bi-prod.is.keysight.com/MicroStrategy/servlet/mstrWeb"))

#wait for the element to be visible
def waitForElement(driver, howToLocateElement, element):
    return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((howToLocateElement, element)))

def executeScript(driver, element):
    driver.execute_script("arguments[0].click();", waitForElement(driver, By.XPATH, element))

def downloadWait():
    dl_wait = True
    while dl_wait:
        sleep(1)
        dl_wait = False
        #go through the file name in the downloads folder
        for fname in os.listdir(PATH_TO_DOWNLOADS):
            if fname.endswith('.crdownload'):
                dl_wait = True
    print("File Download Complete")

def makeDosierReport(driver):
    folders = ["//a[text() = 'Financial Reporting']", "//div[text() = 'Shared Reports']", "//a[text() = 'Function Specific Content']", "//a[text() = 'Marketing']", "//a[text() = 'KGM - Concur Detail Report']", "//input[@value = 'Run Dossier']"]
    for folder in folders:
        executeScript(driver, folder)

makeDosierReport(driver)
sleep(10)
"""
Next step:
- find out how to download the data
- note to self, angular is a mess to us selenium on

theory:
- respond when the elements are present
- locate the more options menu for the concur detail report
- select export
- select data
- wait for download to occur
"""                              