from selenium import webdriver
# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
url="http://google.com"
web=driver.get(url)
kli=driver.find_element_by_name('q')
kli.send_keys('Hitler')
kli2=driver.find_element_by_id('gb_70')
kli2.click()
kli3=driver.find_element_by_xpath('//*[@id="identifierId"]')
kli3.send_keys('benjamin.vlaisavljevikj@deptagency.com')
driver.implicitly_wait(5)
kli4=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
kli4.click()
driver.implicitly_wait(5)
kli5=driver.find_element_by_name('password')
kli5.send_keys('#Planini14')
kli6=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
kli6.click()
if 1:
    print ('all is good')
driver.quit()