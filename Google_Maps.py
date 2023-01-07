from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(2)


def searchplace():
    Place = driver.find_element(By.XPATH,"//input[@id='searchboxinput']")
    Place.send_keys("Tiruchirappalli")
    Submit = driver.find_element(By.XPATH,
        "//button[@id='searchbox-searchbutton']")
    Submit.click()


searchplace()


def directions():
    sleep(5)
    directions = driver.find_element(By.XPATH,"//img[@alt='Directions']")
    directions.click()


directions()


def find():
    sleep(5)
    find = driver.find_element(By.XPATH,"//input[@placeholder='Choose starting point, or click on the map...']")
    find.send_keys("Tirunelveli")
    sleep(2)
    search = driver.find_element(By.XPATH,
        "//div[@id='directions-searchbox-0']//button[@aria-label='Search']")
    search.click()


find()


def time_needed():
    sleep(3)
    Bus_km = driver.find_element(By.XPATH,
       "//div[contains(text(),'294 km')]")
    print("Bus Travel Km:", Bus_km.text)
    Bus_time=driver.find_element(By.XPATH,"//span[normalize-space()='4 hr 19 min']")
    print("Bus Travel time:", Bus_time.text)
    sleep(8)



time_needed()
