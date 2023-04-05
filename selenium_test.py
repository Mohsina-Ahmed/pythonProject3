from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url="https://www.amazon.co.uk/Tefal-Capacity-Programs-EY801827-Exclusive/dp/B0BFFQD43H/ref=sr_1_1_sspa?crid=B02SDI9YO5TW&keywords=air+fryers&qid=1679670560&sprefix=Air%2Caps%2C91&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
driver.get(url)
#price = driver.find_element_by_class_name("a-offscreen")
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
price_attribute_value = price.get_attribute('value')
print(price)
print(price_attribute_value)
print ('price.text: {0}'.format(price.text))
#print("Price is: " + price.text)
#driver.close()
driver.quit()

