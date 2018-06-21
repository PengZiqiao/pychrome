from os import system as cmd
from selenium import webdriver
from selenium.webdriver import ChromeOptions

PORT = 8888
DRIVER_PATH = 'C:/webdrivers/chromedriver.exe'
CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

cmd(f'"{CHROME_PATH}" --remote-debugging-port={PORT}')

options = ChromeOptions()
options.debugger_address = f'127.0.0.1:{PORT}'
driver = webdriver.Chrome(
    executable_path=DRIVER_PATH, chrome_options=options)
