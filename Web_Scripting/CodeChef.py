from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import Excel as ex


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.codechef.com/practice")
driver.maximize_window()
time.sleep(10)

buttom = driver.find_element(By.CSS_SELECTOR, "#pagination-next > span.MuiIconButton-label > svg")


def Elements():
    tb = "#MUIDataTableBodyRow-"
    code = " > td:nth-child(1) > div"
    name = " > td:nth-child(2) > div > span"
    diff = " > td:nth-child(4) > div"
    soup = BeautifulSoup(driver.page_source, 'lxml')
    s = soup.select_one("#pagination-rows")
    no_of_problem = int(s.text)
    for i in range(0, no_of_problem):
        
        element = soup.select_one(tb + str(i))
        n = element.select_one(tb + str(i) + name)
        c = element.select_one(tb + str(i) + code)
        d = element.select_one(tb + str(i) + diff)

        l.append([n.text, furl + c.text, int(d.text)])
    
    f = soup.select_one("#pagination-next > span.MuiIconButton-label > svg").attrs
    if 'disabled' in f.keys():
        return False
    else:
        buttom.click()
        return True

    

soup = BeautifulSoup(driver.page_source, 'lxml')
l = [["Name", "URL", "Difficulty"],]

furl = "https://www.codechef.com/problems/"

n = soup.select_one("#pagination-next > span.MuiIconButton-label > svg").attrs

i = 1 
if 'disabled' in n.keys():
    print("No pages found")
else:
    while True:
        print(f"Page {i} is fetching...")
        b = Elements()
        print(f"Page {i} is done\n\n")
        time.sleep(5)
        i += 1
        if b == False:
            break

driver.quit()


print("*****Done all pages*****")
print(f"Total {l.__len__()-1} questions fetched")
ex.xcelSheet("CodeChef", "Questions", l)


