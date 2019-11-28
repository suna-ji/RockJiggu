import webbrowser
import requests
import os
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

driver = webdriver.Chrome("./chromedriver")

user_id = 'rockjiggu16@gmail.com'
user_pw = 'rockrock16!!'


driver.get("https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_youraccount_orders&pageId=webcs-yourorder&showRmrMe=1")
driver.execute_script("document.getElementsByName('email')[0].value = \'"+user_id+"\'")
driver.find_element_by_xpath('//*[@id="continue"]').click()	
driver.execute_script("document.getElementsByName('password')[0].value = \'"+user_pw+"\'")
driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()