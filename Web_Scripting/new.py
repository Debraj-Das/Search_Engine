from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()

input = driver.find_element(By.CSS_SELECTOR , "#APjFqb")

input.send_keys("codeforces")

search = driver.find_element(By.CSS_SELECTOR , "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
search.click()

code = driver.find_element(By.CSS_SELECTOR , "#rso > div:nth-child(1) > div > div > div > div > div > div > div > div.yuRUbf > a > h3")
code.click()

problem = driver.find_element(By.CSS_SELECTOR, "#body > div.roundbox.menu-box.borderTopRound.borderBottomRound > div > ul > li:nth-child(6) > a")
problem.click()


n = driver.find_element(By.CSS_SELECTOR, "#pageContent > div.pagination > ul > li:nth-child(6) > span > a")
n.click()



time.sleep(30)
# not quit the windows after the execution
driver.quit()
