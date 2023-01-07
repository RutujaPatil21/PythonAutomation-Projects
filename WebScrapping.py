from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import openpyxl
import smtplib
from email.message import EmailMessage

driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://amazon.in/")
sleep(2)
act=ActionChains(driver)

# to search the particular product
def search():
    product=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("samsung phones")
    act.click(product)
    driver.find_element(By.ID,"nav-search-submit-button").click()

    # to filter the samsung phones , click on samsung checkfox in filters on left side
    driver.find_element(By.XPATH,"//li[@id='p_89/Samsung']//i[@class='a-icon a-icon-checkbox']").click()

search()

# get list of the phones and their prices
def get_product_info():

    # get list of phones
    phones=driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")

    #get list of prices
    prices=driver.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")

    # make a list to add all the product info
    my_phones = []
    my_price = []

    for i in phones:
        #print(i.text)

        # add each value in this list
        my_phones.append(i.text)

    for p in prices:
        #print(p.text)

        # add each value in this list
        my_price.append(p.text)

    # use "zip" tp zip both the list phones and prices
    final_list = zip(my_phones, my_price)


    # save data to excel
    wb = openpyxl.Workbook()
    sheet = wb.active

    for x in list(final_list):
        sheet.append(x)

    wb.save("webscrapping_Data.xls")

get_product_info()

# send the above file as email

msg=EmailMessage()
msg['Subject']='Test email'
msg['From']='patil.rutuja021@gmail.com'
msg['To']='patilrutuja211998@gmail.com'
msg.set_content(" I am practicing automation ")

with open('Email_template.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

with open("webscrapping_Data.xls") as f:
    file_data=f.read()
    print("File data in bunary",file_data)
    file_name=f.name
    print("File name is ",file_name)
    msg.add_attachment(file_data,maintype="application",subtype='xls',file_name=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server
    server.login("sendermail@gmail.com","password")
    server.send_message(msg)
    
print("Mail Sent")
















driver.close()

