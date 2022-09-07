from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\Users\\mchdr\\Desktop\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.forward()
driver.refresh()
driver.close()

