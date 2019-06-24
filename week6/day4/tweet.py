from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "https://twitter.com/srivasaava"

sleep(1)

browser = webdriver.Chrome("C:/Users/User/Downloads/chromedriver.exe")# go to url
browser.get(url)
mailid= browser.find_element_by_xpath('//*[@id="search-query"]')#fetching name

id1='@pareekkhushbu51'
mailid.send_keys(id1)#feeding inputs


sleep(2)

login=browser.find_element_by_xpath('//*[@id="global-nav-search"]/span/button')

login.click()


text1=browser.find_element_by_xpath('//*[@id="page-container"]/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[2]/a/span[3]').text

print('Your followers:\n' + text1 )


sleep(5)
 

browser.quit()
