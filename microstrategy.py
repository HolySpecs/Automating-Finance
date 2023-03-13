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
DOWNLOAD_REQUEST_DELAY = 5
DELAY_UNTIL_TIMEOUT = 180

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.get("https://bi-prod.is.keysight.com/MicroStrategy/servlet/mstrWeb")
#wait for the user to enter their details
WebDriverWait(driver, DELAY_UNTIL_TIMEOUT).until(EC.url_to_be("https://bi-prod.is.keysight.com/MicroStrategy/servlet/mstrWeb"))

#wait for the element to be visible
def waitForElement(driver, howToLocateElement, element):
    return WebDriverWait(driver, DELAY_UNTIL_TIMEOUT).until(EC.element_to_be_clickable((howToLocateElement, element)))

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

def downloadDosierReport(driver):
    #waitForElement(driver, By.XPATH, "//div[@id = 'mstr136' and @class = 'mstrmojo-VIDocLayoutViewer ']")
    executeScript(driver, "//div[@class = 'hover-btn hover-menu-btn mouse-left' and @aria-label = 'Context Menu']")
    executeScript(driver, "//*[text() = 'Export']")
    executeScript(driver, "//*[text() = 'Data']")
    sleep(DOWNLOAD_REQUEST_DELAY)
    downloadWait()

makeDosierReport(driver)
downloadDosierReport(driver)                         