from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv

#open the mciindia.org page
driver = webdriver.Chrome(executable_path="C:\Users\Shashank Gupta\Desktop\chromedriver")
driver.get("http://mciindia.org/InformationDesk/IndianMedicalRegister.aspx")
assert "Indian Medical" in driver.title

#click on search-by State Medical Council link
elem = driver.find_element_by_id("dnn_ctr588_IMRIndex_Link_Council")
elem.click()

srno=0
def read_values():
	name = driver.find_element_by_id("Name").text
	regno = driver.find_element_by_id("Regis_no").text
	regdate = driver.find_element_by_id("Date_Reg").text
	address = driver.find_element_by_id("Address").text
	global srno
	srno += 1
	with open('selenium.csv', 'ab') as csvfile:
		spamwriter = csv.writer(csvfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([srno,name,regno,regdate,address])

#the following function grabs all the view-links and visits them....for this selenium required to
#switch between windows....for that it required the handles of both the windows in that particular 
#session (they change in every session)....driver.window_handles returns handles of all the windows
#in current session
def view_and_cancel():
	while True:
		list_views = driver.find_elements_by_link_text('View')
		for view in list_views:
			view.click()
			handles = driver.window_handles
			driver.switch_to_window(handles[1])
			read_values()
			driver.find_element_by_xpath('//*[@id="Btn_Cancel"]')
			driver.switch_to_window(handles[0])

	#on running this while loop it successfully selects the next state council on reaching the last list
	#of entries for a particular list but for the next option starts from the same number where it previously left
	#hence include try except in the calling function to select next option from text box whether 
	#or not 'first' exists for that page
		try:
			next = driver.find_element_by_partial_link_text('Next')
			next.click()
			continue
		except NoSuchElementException:
			return

#select each state one by one and click submit!
for i in range(2,42):
	try:
		first = driver.find_element_by_partial_link_text('First')
		first.click()
		textBox = driver.find_element_by_xpath("//select[@id='dnn_ctr588_IMRIndex_Drp_StateCouncil'][@name='dnn$ctr588$IMRIndex$Drp_StateCouncil']")
		option = textBox.find_element_by_xpath("//option[%d]" % i)	
		option.click()
		driver.find_element_by_xpath("//input[@name='dnn$ctr588$IMRIndex$Submit_Btn'][@id='dnn_ctr588_IMRIndex_Submit_Btn']").click()
		view_and_cancel()
	except NoSuchElementException:
		textBox = driver.find_element_by_xpath("//select[@id='dnn_ctr588_IMRIndex_Drp_StateCouncil'][@name='dnn$ctr588$IMRIndex$Drp_StateCouncil']")
		option = textBox.find_element_by_xpath("//option[%d]" % i)	
		option.click()
		driver.find_element_by_xpath("//input[@name='dnn$ctr588$IMRIndex$Submit_Btn'][@id='dnn_ctr588_IMRIndex_Submit_Btn']").click()
		view_and_cancel()

driver.close()