from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\mchdr\\Desktop\\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']").send_keys("Michal")
driver.find_element(By.NAME, "email").send_keys("Michal@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("example123")
driver.find_element(By.ID, "exampleCheck1").click()

dropdown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")

driver.find_element(By.NAME, "bday").send_keys("26061997")
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)

assert "Success" in message

#driver.close()





