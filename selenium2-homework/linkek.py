# 001-es feladat
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
PATH = "C:\\Users\\Emese\\OneDrive\\Asztali gép\\driver\\chromedriver.exe"
URL = "http://localhost:9999"

try:
    browser = webdriver.Chrome(PATH)
    browser.maximize_window()

    browser.get(URL)

    links_list = []
    # links = browser.find_elements_by_xpath("//a")
    links = browser.find_elements_by_tag_name("a")
    for i in links:
        links_list.append(i.get_attribute("href"))
    print(links_list)

    print(len(links_list))
except:
    print("Something went wrong")

