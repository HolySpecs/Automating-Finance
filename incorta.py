import getpass, os
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

PATH_TO_DOWNLOADS = str(Path.home() / "Downloads")
DOWNLOAD_REQUEST_DELAY = 5

"""
tenant = "Keysight"
username = "nichhenr"
password = "Hydr0C@rb0n$"
"""

tenant = input("Enter the Tenant: ") #Keysight
username = input("Enter your username: ") #nichhenr
password = getpass.getpass("Enter your password for Incorta: ")
favorited = (input("Do you have the locations of the files favorited? (y/n)")).upper()

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get("https://lincortap.cos.is.keysight.com:8443/incorta/#/login")

#logging the user in
def login(driver, tenant, username, password):
    #enter the correct details in the login page
    tenantField = driver.find_element(By.ID, "tenant")
    usernameField = driver.find_element(By.ID, "username")
    passwordField = driver.find_element(By.ID, "password")
    signInButton = driver.find_element(By.CSS_SELECTOR, "button")
    tenantField.send_keys(tenant)
    usernameField.send_keys(username)
    passwordField.send_keys(password)
    sleep(1)
    signInButton.click()

#wait for the element to be visible
def waitForElement(driver, howToLocateElement,element):
    return WebDriverWait(driver, 30).until(EC.presence_of_element_located((howToLocateElement, element)))

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

def backToHome(driver):
    clickableLogo = driver.find_element(By.CLASS_NAME, "inc-clickable-wrapper")
    clickableLogo.click()
    sleep(1)

def goToLocation(driver):
    folders = ["//a[text() = 'Marketing'", "//a[text() = 'Marcom Reports'"]
    for folder in folders:
        waitForElement(driver, By.XPATH, folder).click()

def downloadCSVReport(driver):
    MoreOptionsHeader= driver.find_element(By.XPATH, "//div[@class = 'draggable-insight-wrapper']")
    MoreOptionsButton = driver.find_element(By.XPATH, "(//button[@class = 'insight__header-menu kebab-icon ant-dropdown-trigger'])[1]")
    hover = ActionChains(driver).move_to_element(MoreOptionsHeader).move_to_element(MoreOptionsButton).click()
    hover.perform()
    downloadOption = waitForElement(driver, By.XPATH, "//li[@aria-label = 'Download']")
    hover = ActionChains(driver).move_to_element(downloadOption)
    hover.perform()
    csvOption = waitForElement(driver, By.XPATH, "//button[@class = 'inc-clickable ' and @tabindex = '0']/span[@class = 'inc-clickable-wrapper']")
    hover = ActionChains(driver).move_to_element(csvOption).click()
    hover.perform()
    #wait for the file to appear in downloads
    sleep(DOWNLOAD_REQUEST_DELAY)
    #wait until the download is complete
    downloadWait()

def downloadPoReport(driver, favorited):
    if favorited == "N":
        goToLocation(driver)
    PoReportItem = waitForElement(driver, By.XPATH, "//span[text() = 'MARCOM PO REPORT - PR  Number Copy']")
    PoReportItem.click()
    waitForElement(driver, By.XPATH, "//a[text() = 'Operating Unit Name']")
    downloadCSVReport(driver)

def downloadInvoiceReport(driver, favorited):
    if favorited == "N":
        goToLocation(driver)
    InvoiceItem = waitForElement(driver, By.XPATH, "//span[text() = 'Marcom_Invoices']")
    InvoiceItem.click()
    waitForElement(driver, By.XPATH, "//a[text() = 'Operating Unit ( Invoice)']")
    downloadCSVReport(driver)

login(driver, tenant, username, password)
downloadPoReport(driver, favorited)
backToHome(driver)
downloadInvoiceReport(driver, favorited)
backToHome(driver)