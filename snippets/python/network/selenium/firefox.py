import geckodriver_autoinstaller
from selenium import webdriver

geckodriver_autoinstaller.install()

driver = webdriver.Firefox()

driver.get(f'https://...')
