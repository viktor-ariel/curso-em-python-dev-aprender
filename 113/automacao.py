
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://automatize.netlify.app/')

campo_email = driver.find_element_by_id('email')

campo_email.click()






