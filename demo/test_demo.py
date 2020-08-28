import selenium
from selenium import webdriver
import time;

from selenium.webdriver.common.by import By


def test_demo():
    global driver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("今日头条")
    driver.find_element(By.ID, "su").click()
    driver.quit()