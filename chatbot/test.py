# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time

# # response = requests.get('https://www.amazon.com/gp/sign-in.html')
# # soup =  BeautifulSoup(response.text, 'lxml')
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome('./chromedriver', chrome_options=options)
# time.sleep(0.5)

# # print(soup.prettify())

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--remote-debugging-port=9222")

try:
  driver = webdriver.Chrome('./chromedriver', chrome_options=options)
  driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_youraccount_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")
  s = driver.find_element_by_xpath('//*[@id="continue"]').click()
  print(s)
except Exception as ex:
  print(ex)

driver.quit()