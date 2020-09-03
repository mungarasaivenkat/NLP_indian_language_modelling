from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import wget

url = "http://newsonair.com/Audio-Archive-Search.aspx"
# create a new chrome session
driver = webdriver.Chrome(executable_path='C:/Users/LUCIFER/Downloads/chromedriver.exe')
driver.implicitly_wait(30)
driver.get(url)
#ctl00_ContentPlaceHolder1_program_type_cbl > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(1) > label:nth-child(2)
#Accept terms
accept_button = driver.find_element_by_id("ctl00_ContentPlaceHolder1_program_type_cbl")
accept_button.click()
#Wait 10 seconds for the load
driver.implicitly_wait(10)
#ctl00_ContentPlaceHolder1_Category_name_ddl
select_One = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_Category_name_ddl'))
# select by visible text
select_One.select_by_visible_text('Daily')
#ctl00_ContentPlaceHolder1_program_name_ddl
select_Two = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_program_name_ddl'))
# select by visible text
select_Two.select_by_visible_text('Samachar Darshan')
find_button = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Button1')
find_button.click()
#Wait 10 seconds for the load
driver.implicitly_wait(10)
links = driver.find_elements_by_tag_name('audio')
for link in links:
    source = link.get_attribute('src')
    if source is not None :
        print(source)
        print('\n')
    wget.download(source,'C:/Users/LUCIFER/Desktop/dataset')