from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
def cb(path):
    login = browser.find_element_by_xpath(path)
    login.click()

browser = webdriver.Chrome('driver\chromedriver_win32\chromedriver.exe')

browser.get('https://www.costcotravel.ca/')

cb('//*[@id="provincePopupDiv"]/div/div/div/div[2]/div/div[9]/label') # Ontario

cb('//*[@id="provincePopupDiv"]/div/div/div/div[2]/button')# Continue
cb('//*[@id="rental-cars-tab-id"]')  # rental cars

address='//*[@id="pickupLocationTextWidget"]'
inadd=browser.find_element_by_xpath(address)

ad='//*[@id="pickup_location_widget"]/div/ul/li'
inadd.send_keys('M2N (North York, ON, CA)')
time.sleep(2)
#cb(ad)
update='//*[@id="pickUpDateWidget"]'
update='//*[@id="pickup_date_widget"]/button'
cb(update)
thursday='//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[3]/td[5]/a'
thursday='//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[3]/td[5]'
wednesday='//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[3]/td[4]/a'
cb(thursday)
#cb(wednesday)
uptime='//*[@id="pickupTimeWidget"]'
cb(uptime)
sixpm='//*[@id="pickupTimeWidget"]/option[37]'
cb(sixpm)
nineam='//*[@id="pickupTimeWidget"]/option[19]'

offdate='//*[@id="dropoff_date_widget"]/button'
cb(offdate)
monday='//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[4]/td[2]'
cb(monday)
offtime='//*[@id="dropoffTimeWidget"]'

cb(offtime)

cb('//*[@id="dropoffTimeWidget"]/option[37]')

findcar='//*[@id="findMyCarButton"]'

cb(findcar)


time.sleep(3)
nyc='//*[@id="csr_cell_1_3"]/a'  # north york centre location
cb(nyc)
thornhill='//*[@id="csr_cell_4_3"]/a' # Thornhill location
cb(thornhill)
ys='//*[@id="csr_cell_3_3"]/a'  #  yonge sheppard location
cb(ys)

cb('//*[@id="car_rental_map"]/div[3]/div[1]/div/div/div[4]/button')# finalstep