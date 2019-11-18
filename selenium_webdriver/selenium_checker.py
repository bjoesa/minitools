
import time
from selenium import webdriver

url = input('Type your URL: ')  # http://www.google.com/

print(url)

driver = webdriver.Chrome()
# driver = webdriver.Chrome('C:\chromedriver_win32')
driver.get(url)
time.sleep(5) # Let the user actually see something

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

'''

https://sites.google.com/a/chromium.org/chromedriver/getting-started

'''
