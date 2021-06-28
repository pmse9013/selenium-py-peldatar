#015-ös feladat
from selenium import webdriver

PATH = "C:\\Users\\Emese\\OneDrive\\Asztali gép\\driver\\chromedriver.exe"
URL = "http://localhost:9999/todo.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)

active = browser.find_elements_by_xpath("//span[@class='done-false']")
for i in active:
    print(i.get_attribute("textContent"))