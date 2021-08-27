from time import sleep
from selenium import webdriver

# 启动浏览器
driver = webdriver.Firefox()
driver.get('https://nymalltest.shop/login.html#/')
sleep(2)
driver.find_element_by_id('username').send_keys('jsce01')
driver.find_element_by_id('password').send_keys('000000')
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(2)
driver.switch_to.frame()
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')

