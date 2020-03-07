''' 
#Start
#      - start the browser (Firefox or Chrome) and open ' https://alteryx-automation.herokuapp.com/ ';
#
#   Second Page
#
#      - on the second page: find a "secret code" input element and enter its value into the input field;
#
#      - ensure that the checkbox is checked;
#
#   Success Page
#
#      - ensure that last page has information about successful entering of secret code.
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(2)
driver.get("https://alteryx-automation.herokuapp.com/")
btn_enter = driver.find_element_by_id("enter")
btn_enter.click()
assert "secret_code" in  driver.current_url

cbox = driver.find_element_by_id("checkbox")
scode = driver.find_element_by_id("secret_code")
btn_submit = driver.find_element_by_id("submit")
inpt_secret = driver.find_element_by_css_selector("#root > div > div > div:nth-child(3) > input")
inpt_secret.send_keys(scode.get_attribute("value"))
if cbox.get_attribute('checked'): 
	pass
else: 
	cbox.click()
btn_submit.click()


driver.implicitly_wait(2)
success_str = "SUCCESS"
assert success_str.lower() in driver.current_url
lbl_result = driver.find_element_by_id("result")
assert "SUCCESS" in lbl_result.text

driver.close()