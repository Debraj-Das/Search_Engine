from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import Excel as ex

from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                        options=options)
driver.implicitly_wait(10)
driver.get("https://www.codechef.com/practice")
driver.maximize_window()
time.sleep(10)

buttom = driver.find_element(By.CSS_SELECTOR, "#pagination-next > span.MuiIconButton-label > svg")


# #MUIDataTableBodyRow-0 > td:nth-child(1) > div
# #MUIDataTableBodyRow-0 > td:nth-child(2) > div > span
# #MUIDataTableBodyRow-0 > td:nth-child(4) > div


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
    while i<3:
        print(f"Page {i} is fetching...")
        b = Elements()
        print(f"Page {i} is done\n\n")
        time.sleep(5)
        i += 1
        if b == False:
            break


print("*****Done all pages*****")
print(f"Total {l.__len__()-1} questions fetched")
ex.xcelSheet("CodeChef", "Questions", l)










# no = len(s)
# no_of_page = len(s)

# print(no, " pages found\n")





#*  




# buttomClick = driver.find_element(By.CSS_SELECTOR, "#root > div > div._pageContainer_1se0b_3._dark_1se0b_9 > div > div._fullWidth_1uro6_2 > div > div._rightColumnContainer_1a63v_11 > div > div:nth-child(3) > div > table > tfoot > tr > td > div > div.MuiToolbar-root.MuiToolbar-regular.MuiToolbar-gutters > div > div")
# c.click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# number = driver.find_element(By.CSS_SELECTOR , "#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(2)")
# number.click()




# #root > div > div._pageContainer_1se0b_3._dark_1se0b_9 > div > div._fullWidth_1uro6_2 > div > div._rightColumnContainer_1a63v_11 > div > div:nth-child(4) > div > div.jss3974 > table > thead > tr
# #root > div > div._pageContainer_1se0b_3._dark_1se0b_9 > div > div._fullWidth_1uro6_2 > div > div._rightColumnContainer_1a63v_11 > div > div:nth-child(4) > div > div.jss637 > table > tbody


# <div class="MuiToolbar-root MuiToolbar-regular MuiTablePagination-toolbar jss2440 MuiToolbar-gutters"><div class="MuiTablePagination-spacer"></div><p class="MuiTypography-root MuiTablePagination-caption MuiTypography-body2 MuiTypography-colorInherit" id="mui-25571">Rows per page:</p><div class="MuiInputBase-root MuiTablePagination-input MuiTablePagination-selectRoot jss2441"><div class="MuiSelect-root MuiSelect-select MuiTablePagination-select MuiSelect-selectMenu MuiInputBase-input" tabindex="0" role="button" aria-haspopup="listbox" aria-labelledby="mui-25571 pagination-rows" id="pagination-rows" data-testid="pagination-rows" fdprocessedid="z119e8">20</div><input aria-hidden="true" tabindex="-1" class="MuiSelect-nativeInput" value="20"><svg class="MuiSvgIcon-root MuiSelect-icon MuiTablePagination-selectIcon" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 10l5 5 5-5z"></path></svg></div><p class="MuiTypography-root MuiTablePagination-caption MuiTypography-body2 MuiTypography-colorInherit">1-20 of 4204</p><div class="MuiTablePagination-actions"><button class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit Mui-disabled Mui-disabled" tabindex="-1" type="button" title="Previous Page" aria-label="Previous Page" id="pagination-back" data-testid="pagination-back" fdprocessedid="mzwnuo" disabled=""><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.41 16.09l-4.58-4.59 4.58-4.59L14 5.5l-6 6 6 6z"></path></svg></span></button><button class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit" tabindex="0" type="button" title="Next Page" aria-label="Next Page" id="pagination-next" data-testid="pagination-next" fdprocessedid="yhnzsq"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.59 16.34l4.58-4.59-4.58-4.59L10 5.75l6 6-6 6z"></path></svg></span><span class="MuiTouchRipple-root"></span></button></div></div>







# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--incognito')
# options.add_argument('--headless')

#         # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#         # headless browser
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                         options=options)

# pageurl = "https://www.codechef.com/practice"

# driver.get(pageurl)
# driver.maximize_window()

# driver.implicitly_wait(10)



# #menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(1)


# with open("output1.html", "w", encoding = 'utf-8') as file:
#     # prettify the soup object and convert it into a string  
#     file.write(str(soup.prettify()))
