#This code has no guarantees of correctness or security.

import sys
import urllib.request
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup as BSHTML
import re
from collections import namedtuple

import time

from contextlib import closing

from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

ACard = namedtuple("ACard", "name percent count")	



#myProxy = "http://proxy.com:911"

#service_args = [
#    '--proxy=http://proxy.com:911'
#    ]
	
#timeframe = "2months"
timeframe = "2weeks"
	
#format="Modern"
format="Standard"
	
date = time.strftime("%x")
current_time = time.strftime("%X")
current_time = current_time.replace(':','.')
file_name = "C:\\temp\\"+format+"\\"+timeframe+"\\meta_log." + date.replace('/','.') +"."+current_time+"_"+timeframe+".txt"
out_file = open(file_name, 'w+')
	
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\temp\AppData\\Local\\Google\\Chrome\\tempID")
options.add_argument("service_log_path='C:\\temp\\ghostdriver.log")
options.add_argument('service_args=--silent')
#options.add_argument("proxy=http://proxy.com:911")

driver = webdriver.Chrome("C:\\Users\\temp\\Desktop\\temp\\chromedriver.exe",chrome_options=options)
driver.set_window_size(1120, 550)
driver.get("http://mtgtop8.com/topcards")
select = Select(driver.find_element_by_name('format'))
select.select_by_visible_text(format)
#select.select_by_visible_text('Modern')

if(format=='Modern'):
	select = Select(driver.find_element_by_id('meta_MO'))
	#select.select_by_visible_text('Last 2 Weeks')
elif(format=='Standard'):
	select = Select(driver.find_element_by_id('meta_ST'))

if(timeframe == "2weeks") :
	select.select_by_visible_text('Last 2 Weeks')
elif(timeframr == "2months"):
	select.select_by_visible_text('Last 2 Months')
else:
	print("No timeframe found!")
	sys.exit(1)
	
driver.find_element_by_id('lands').click()

#try and click go button
found = False
try:
	driver.find_element_by_xpath("//html//body//div[3]//div//table//tbody//tr[1]//td/table//tbody//tr[1]//td[4]//input").click()
	found = True
except NoSuchElementException :
	print("Button not in div[3]")
	found = False
if(found != True) :
	try:
		driver.find_element_by_xpath("//html//body//div[5]//div//table//tbody//tr[1]//td//table//tbody//tr[1]//td[4]//input").click()
		found = True
	except NoSuchElementException :
		print("Button not in div[5]")
		found = False
if(found != True) :
	try:
		driver.find_element_by_xpath("//html//body//div[4]//div//table//tbody//tr[1]//td//table//tbody//tr[1]//td[4]//input").click()
		found = True
	except NoSuchElementException :
		print("Button not in div[4]")
		found = False
html_source = driver.page_source
lines = html_source.split('\n')
lit = iter(lines)
AffCount=0

while True:
	try :
		l = next(lit)
		if ((l.find("AffCard") != -1) and (AffCount<2)):
			AffCount += 1
		elif(l.find("AffCard") != -1) :
			l = next(lit)
			card_name = l.split('>')[1].split('<')[0]
			l = next(lit)
			card_per = l.split('>')[1].split('<')[0].split(' ')[0]
			l = next(lit)
			card_count = l.split('>')[1].split('<')[0]
			c = ACard(name = card_name, percent = card_per, count = card_count)
			print(c.name + " / " + c.percent + " / " + c.count)
			out_file.write(c.name + " / " + c.percent + " / " + c.count +'\n')
			#print(l)
	except StopIteration:
		break

driver.find_element_by_class_name('Nav_PN').click()

for i in range(10) :
	html_source = driver.page_source
	lines = html_source.split('\n')
	lit = iter(lines)
	AffCount=0
	while True:
		try :
			l = next(lit)
			if ((l.find("AffCard") != -1) and (AffCount<2)):
				AffCount += 1
			elif(l.find("AffCard") != -1) :
				l = next(lit)
				card_name = l.split('>')[1].split('<')[0]
				l = next(lit)
				card_per = l.split('>')[1].split('<')[0].split(' ')[0]
				l = next(lit)
				card_count = l.split('>')[1].split('<')[0]
				c = ACard(name = card_name, percent = card_per, count = card_count)
				print(c.name + " / " + c.percent + " / " + c.count)
				out_file.write(c.name + " / " + c.percent + " / " + c.count+'\n')
				#print(l)
		except StopIteration:
			break
	try:				#driver.find_element_by_xpath("//html//body//div[3]//div//table//tbody//tr[2]//td//table//tbody//tr[2]//td//table//tbody//tr//td//table//tbody//tr//td[10]//div").click()
	#driver.find_element_by_class_name("Nav_PN").click()
		tmp = driver.find_elements_by_class_name('Nav_PN')
		try:
			tmp[1].click()
		except IndexError:
			print("Can't click next button!")
			break
		#select.select_by_visible_text('Next').click()
	except NoSuchElementException :
		print("Next Button not found")
		break
out_file.close()
tmp = input('press enter to quit ')
#print(driver.find_elements_by_xpath("/html/body/div[3]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[1]/select"))
#driver.find_element_by_xpath("/html/body/div[3]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[1]/select[@id='format']/option[@value='MO']").click()
#for entry in driver.get_log('browser'):
#    print(entry)

driver.quit()
#wait(5)
#ids = driver.find_elements_by_xpath('//*[@id="priceTable"]/tr[1]/td[3]/span[1]')
#ids = driver.find_element_by_class_name('scActualPrice largetext pricegreen')
#driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
#driver.find_element_by_id("search_button_homepage").click()
#print( driver.current_url)
sys.exit()
print("5")
