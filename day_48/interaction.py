from selenium import webdriver

chrome_driver_path_wsl="/usr/bin/chromedriver"

driver=webdriver.Chrome(executable_path=chrome_driver_path_wsl)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_of_articles=driver.find_element_by_css_selector("#articlecount a")
print(f"{num_of_articles.text} articles")

driver.quit()