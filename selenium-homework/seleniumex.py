#008 - as feladat
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
PATH = "C:\\Users\\Emese\\OneDrive\\Asztali gép\\driver\\chromedriver.exe"
URL = "https://webshop.progmasters.hu/"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)

try:
    browser.find_element_by_id("nemletezik")
except NoSuchElementException as error:
    print("No such element")

# EXTRA feladat
# def id_no_such_element(id):
#     try:
#         browser.find_element_by_id(id)
#     except NoSuchElementException as error:
#         print("No such element")
#
# id_no_such_element("nemletezo")



