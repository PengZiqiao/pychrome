from os import system as cmd
from selenium import webdriver
from selenium.webdriver import ChromeOptions

cmd('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8888')

options = ChromeOptions()
options.debugger_address = '127.0.0.1:8888'
executable_path = 'c:/webdrivers/chromedriver.exe'
driver = webdriver.Chrome(
    executable_path=executable_path, chrome_options=options)
