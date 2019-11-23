from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
time.sleep(0.5)

driver.get("https://world.taobao.com/markets/all/login?spm=a21wu.241046-kr.7607074463.12.41cab6cbKf78g7")
id_box = driver.find

<input type="text" name="TPL_username" id="TPL_username_1" class="login-text J_UserName" value="" maxlength="32" tabindex="1" aria-label="会员名/邮箱">