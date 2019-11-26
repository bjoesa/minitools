from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


''' 

INFO SOURCE:

https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver/52572919#52572919

'''

''' URL parsing '''
#url = input('Type your URL (cp&paste https://de.iqos.com/de/produkte): ') 
#print(url)

''' file name '''
timestr = time.strftime("%Y%m%d-%H%M%S")
print('TIME STRING', timestr)

''' Chrome options '''
c_options = Options()
c_options.add_argument('--headless')    # needed for fullpage screenshot
# c_options.add_argument('--start-maximized')

''' Start driver '''
driver = webdriver.Chrome(options=c_options)
#driver.get(url)
# driver.get('https://de.iqos.com/de/')
driver.get('https://preprod.iqos.de/de/produkte/iqos-3-info')

''' wait until page is loaded '''
time.sleep(2)

''' cross gates '''
cookie_button = driver.find_element_by_id('cookie-accept-close')
cookie_button.click()

age_button = driver.find_element_by_id('age-gate-yes')
age_button.click()

''' wait until page is loaded '''
time.sleep(5)

''' fullpage screenshot '''

#the element with longest height on page
# ele = driver.find_element("xpath", '//div[@class="react-grid-layout layout"]')
# total_height = ele.size["height"]+1000

element = driver.find_element_by_tag_name('body')
total_body_height = element.size["height"]

print('total_body_height:', total_body_height)

driver.set_window_size(1920, total_body_height)      #the trick
print('driver.get_window_size',	driver.get_window_size())

driver.refresh

print('driver.get_window_size',	driver.get_window_size())

time.sleep(5)

element_png = element.screenshot_as_png

time.sleep(2)

# driver.save_screenshot("selenium_webdriver/shots/1920px-screenshot1-" + timestr + ".png")

print(driver.current_url)
name = driver.name
print(driver.name)
# orientation = driver.orientation
# print(driver.orientation)

with open("selenium_webdriver/shots/1920px-test2-" + timestr + ".png", "wb") as file:
    file.write(element_png)

time.sleep(2) # Öffnet den Browser für X Sekunden
# driver.quit()
driver.close()
