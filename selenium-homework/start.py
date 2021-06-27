#006 - os feladat
from selenium import webdriver
PATH = "C:\\Users\\Emese\\OneDrive\\Asztali gép\\driver\\chromedriver.exe"
URL = "https://webshop.progmasters.hu/"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)
