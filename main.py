from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
chop = webdriver.ChromeOptions()
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chop)
browser.maximize_window()

browser.get("http://thetenthwatch.com/")

try:
	element = WebDriverWait(browser, 1000).until(
		ec.presence_of_element_located((By.XPATH, r'/html/body/div[3]/div[2]/div/div/div/div/a')))
finally:
	browser.find_element_by_xpath(r'/html/body/div[3]/div[2]/div/div/div/div/a').click()

for i in range(1, 400):
	browser.execute_script('''window.open("''' + 'http://thetenthwatch.com/' + '''","_blank");''')
	browser.switch_to.window(browser.window_handles[i])
	try:
		element = WebDriverWait(browser, 1000).until(ec.presence_of_element_located((
			By.XPATH, r'/html/body/div[3]/div[2]/div/div/div/div/a')))
	finally:
		browser.find_element_by_xpath(r'/html/body/div[3]/div[2]/div/div/div/div/a').click()
