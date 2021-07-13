from selenium import webdriver
import time
import operator

chrome_driver_path_wsl="/usr/bin/chromedriver"

driver=webdriver.Chrome(executable_path=chrome_driver_path_wsl)
cookie_clicker_url="http://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_clicker_url)

cookie=driver.find_element_by_id("cookie")

start_time=time.time()
timeout = start_time + 60*5   # 5 minutes from now
every_5_seconds=start_time+5

store_objs=driver.find_elements_by_css_selector("#store b")
store_items=[]
for objs in store_objs:
    store_items.append(objs.text)

store_ids=["#buyCursor","#buyGrandma","#buyFactory","#buyMine","#buyShipment","#buyAlchemy\ lab","#buyPortal","#buyTime\ machine"]
while time.time() < timeout:
   cookie.click()
   if time.time() > every_5_seconds:
       money=int(driver.find_element_by_id("money").text.replace(",",""))
       tmp_dict={}
       for n in range(len(store_items)-1):
           str_price=store_items[n].strip().replace(",","").split("-")[1]
           price=int(str_price)
           if money>price:
               tmp_dict[n]=price
       highest_buyable=max(tmp_dict, key=tmp_dict.get)
       item_purchase_btn=driver.find_element_by_tag_name(store_ids[highest_buyable])
       item_purchase_btn.click()
       every_5_seconds+=5

result=driver.find_element_by_id("cps").text
print(result)


