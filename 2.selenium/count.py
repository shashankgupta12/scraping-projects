#program to find the total number of doctors registered at mciindia.org which also gives 
#the total number of doctor records which scrape.py will scrape!!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="C:\Users\Shashank Gupta\Desktop\chromedriver")
driver.get("http://mciindia.org/InformationDesk/IndianMedicalRegister.aspx")
assert "Indian Medical" in driver.title

elem = driver.find_element_by_id("dnn_ctr588_IMRIndex_Link_Council")
elem.click()

sums = 0

def count():
	try:
		count = driver.find_element_by_id("dnn_ctr588_IMRIndex_Lbl_Count")
		str1 = count.text
		count =  [int(s) for s in str1.split() if s.isdigit()]
		global sums
		sums += count[0]
		print sums
	except NoSuchElementException:
		return

for i in range(2,42):
	try:
		first = driver.find_element_by_partial_link_text('First')
		first.click()
		textBox = driver.find_element_by_xpath("//select[@id='dnn_ctr588_IMRIndex_Drp_StateCouncil'][@name='dnn$ctr588$IMRIndex$Drp_StateCouncil']")
		option = textBox.find_element_by_xpath("//option[%d]" % i)	
		option.click()
		driver.find_element_by_xpath("//input[@name='dnn$ctr588$IMRIndex$Submit_Btn'][@id='dnn_ctr588_IMRIndex_Submit_Btn']").click()
		count()
	except NoSuchElementException:
		textBox = driver.find_element_by_xpath("//select[@id='dnn_ctr588_IMRIndex_Drp_StateCouncil'][@name='dnn$ctr588$IMRIndex$Drp_StateCouncil']")
		option = textBox.find_element_by_xpath("//option[%d]" % i)	
		option.click()
		driver.find_element_by_xpath("//input[@name='dnn$ctr588$IMRIndex$Submit_Btn'][@id='dnn_ctr588_IMRIndex_Submit_Btn']").click()
		count()

print sums #total records 973804!!!
driver.close()