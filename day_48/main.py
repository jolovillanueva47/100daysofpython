from selenium import webdriver
from datetime import datetime
import pprint


pp = pprint.PrettyPrinter(indent=1)
chrome_driver_path_wsl="/usr/bin/chromedriver"

driver=webdriver.Chrome(executable_path=chrome_driver_path_wsl)
url="https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07YBVJRD7/ref=sr_1_1?dchild=1&keywords=nintendo%2Bswitch&qid=1626145546&s=specialty-aps&sr=1-1&th=1"
url2="https://www.python.org/"
driver.get(url2)
#price=driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
# search_bar=driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# documentation_link=driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link=driver.find_element_by_xpath("/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

upcoming_events=driver.find_elements_by_css_selector(".event-widget time")
upcoming_events_name=driver.find_elements_by_css_selector(".event-widget li a")
# print(upcoming_events)

upcoming_events_dict={}
index=0
for event_date,event_name in zip(upcoming_events,upcoming_events_name):
    upcoming_events_dict[index]={"time":event_date.text,"name":event_name.text}
    index+=1

print(upcoming_events_dict)

driver.quit()