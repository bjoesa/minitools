from selenium import webdriver
import time

#url = input('Type your URL (cp&paste https://de.iqos.com/de/produkte): ') 
#print(url)

driver = webdriver.Chrome()
#driver.get(url)
driver.get('https://de.iqos.com/de/')

cookie_button = driver.find_element_by_id('cookie-accept-close')
cookie_button.click()

age_button = driver.find_element_by_id('age-gate-yes')
age_button.click()

time.sleep(15) # Öffnet den Browser für X Sekunden
driver.quit()
