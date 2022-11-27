from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

start_time = time.time() 
test_cases = {
    'case1': None,                      #successful login
    'case2': None,                      #invalid username
    'case3': None,                      #invalid password
    'case4': None,                      #bus availiable
    'case5': None,                      #bus not availiable
    'case6': None,                      #bus booking successful
    'case7': None,                      #showing bill details
    'case8': None,                      #List of buses
    'case9': None,                      #successfully cancel
    'case10':None                       #checking invalid booking id to cancel bus
}

# driver=webdriver.Chrome("C:\webdriver\chromedriver.exe")
url='http://127.0.0.1:8000/'


driver =  webdriver.Chrome("C:\webdriver\chromedriver.exe") 

driver.maximize_window()

driver.get(url)

#invalid username

username = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))
password = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"))
login = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Sign in')]"))

username.send_keys('rot')
password.send_keys('root')

login.click()

invalidcred=driver.find_element_by_xpath("//p[contains(text(),'Provide valid credentials')]").text

if invalidcred=="Provide valid credentials":
    test_cases["case2"]=True

#invalid Password

username = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))
password = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"))
login = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Sign in')]"))

username.send_keys('root')
password.send_keys('oot')

login.click()

invalidpass=driver.find_element_by_xpath("//p[contains(text(),'Provide valid credentials')]").text

if invalidpass=="Provide valid credentials":
    test_cases["case3"]=True

username = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))
password = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"))
login = WebDriverWait(driver, 30).until(
    lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Sign in')]"))


username.send_keys('root')
password.send_keys('root')

login.click()

fb=driver.find_element_by_xpath("//h2[contains(text(),'Find bus')]").text

if fb=="Find bus":
    test_cases["case1"]=True


# invalidcred=driver.find_element_by_xpath("//p[contains(text(),'Provide valid credentials')]").text

# if invalidcred=="Provid valid credentials":
#     test_cases["case2"]=True

source=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))

destination=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"))

date=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/input[1]"))

findbusbtn=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Find bus')]"))


source.send_keys("Pune")
destination.send_keys("Delhi")
date.send_keys("06-11-2022")
findbusbtn.click()

nobuserr=driver.find_element_by_xpath("//h2[contains(text(),'Find bus')]").text

if nobuserr=="Find bus":
    test_cases["case5"]=True



source=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))

destination=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"))

date=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/input[1]"))

findbusbtn=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Find bus')]"))



source.send_keys("Pune")
# time.sleep(1)
destination.send_keys("Mumbai")
# time.sleep(1)
date.send_keys("06-11-2022")
findbusbtn.click()

# busava=driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/form[1]").text

busava1=driver.find_element_by_xpath("//body//h2").text

if busava1=="List of buses":
    test_cases["case4"]=True


busid=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))

noseats=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//body/form[1]/div[2]/div[1]/input[1]"))

bookbus=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Book bus')]"))

busid.send_keys(3)
noseats.send_keys(2)
bookbus.click()

bookconfirm=driver.find_element_by_xpath("//body/h2[1]").text

if bookconfirm=="Booking Confirmation":
    test_cases["case6"]=True

billdetails=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Bill details')]"))
# time.sleep(3)
billdetails.click()
# time.sleep(3)

showbill=driver.find_element_by_xpath("//h4[contains(text(),'Bill Details')]").text
if showbill=="Bill Details":
    test_cases["case7"]=True

cross=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Close')]"))
# time.sleep(3)
cross.click()

ok=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'OK')]"))

ok.click()

lstbuses=driver.find_element_by_xpath("//body//h2").text
if lstbuses=="List of buses":
    test_cases["case8"]=True

# time.sleep(3)

cancelbus=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))
cancel=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Cancel bus')]"))
    
cancelbus.send_keys(42)
# time.sleep(5)
cancel.click()

if driver.current_url=="http://127.0.0.1:8000/seebookings":
    test_cases["case9"]=True

cancelbus=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//input[@id='example-email-input']"))
cancel=WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//button[contains(text(),'Cancel bus')]"))
    
cancelbus.send_keys(2)
# time.sleep(5)
cancel.click()
invalidbookid=driver.find_element_by_xpath("//h1[contains(text(),'Sorry You have not booked that bus')]").text
if invalidbookid=="Sorry You have not booked that bus":
    test_cases["case10"]=True

driver.close()
print(test_cases)
#  passed test cases

passed_test_cases = [test_case for test_case,
                     status in test_cases.items() if status == True]

#  remaining test cases

remaining_test_cases = [test_case for test_case,
                        status in test_cases.items() if status == None]


print('Passed test cases: ', passed_test_cases)

print("*"*50)

print('Remaining test cases: ', remaining_test_cases)




