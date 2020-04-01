#!/Users/dingchao8868/anaconda3/bin/python3

import os
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup

import smtplib

dt = date(2019,10,8).strftime('%d/%m/%Y')

# driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver') )
driver = webdriver.Chrome('/Users/dingchao8868/Documents/GitHub/automatic-ticket-checking/chromedriver')

driver.get("https://venta.renfe.com")
time.sleep(2)
driver.find_element_by_link_text('Welcome').click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='estacionOrigen_DescEstacion']").send_keys('BARCELONA (TODAS)')
time.sleep(2)
ActionChains(driver).send_keys(Keys.TAB).perform()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='estacionDestino_DescEstacion']").send_keys('MADRID (TODAS)')
time.sleep(2)
ActionChains(driver).send_keys(Keys.TAB).send_keys(dt).perform()
time.sleep(2)
driver.find_element_by_xpath("//button[@title='BUY']").click()
time.sleep(5)
page_html = driver.page_source
page_soup = BeautifulSoup(page_html, "html.parser")
info = page_soup.find(name='p',attrs={'id':'tab-mensaje_contenido'}).string
driver.close()



if info == None:

	EMAIL_ADDRESS = 'xxx@gmail.com'
	EMAIL_PASSWORD = 'xxx'

	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	    smtp.ehlo()
	    smtp.starttls()
	    smtp.ehlo()
	    
	    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	    
	    subject = 'Renfe tickets check on ' + time.ctime()
	    body = 'Tickets are availale on ' + dt + '!!!!!!!!!!!!!!!!!!'
	    
	    msg = f'Subject:{subject}\n\n{body}'
	    
	    smtp.sendmail(EMAIL_ADDRESS, 'dingchaoruc8868@gmail.com', msg)
