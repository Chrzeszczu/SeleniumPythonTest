import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\mchdr\\Desktop\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("Ind")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class$='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break





