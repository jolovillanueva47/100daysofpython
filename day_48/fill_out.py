from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path_wsl="/usr/bin/chromedriver"

driver=webdriver.Chrome(executable_path=chrome_driver_path_wsl)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element_by_name("fName")
first_name.send_keys("Hello")

last_name=driver.find_element_by_name("lName")
last_name.send_keys("World")

email=driver.find_element_by_name("email")
email.send_keys("helloworld@gmail.com")

sign_up_btn=driver.find_element_by_tag_name("button")
sign_up_btn.click()

