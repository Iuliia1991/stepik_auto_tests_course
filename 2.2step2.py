from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.ID, "num1").text
    x_element2 = browser.find_element(By.ID, "num2").text
    y = int(x_element1) + int(x_element2)
    y = str(y)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)
    #browser.find_element(By.TAG_NAME, "select").click()
    #browser.find_element(By.CSS_SELECTOR, "[value= 'y']").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
