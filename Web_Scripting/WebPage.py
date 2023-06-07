from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def WebPage(pageurl, pageTitle):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--incognito')
        options.add_argument('--headless')

        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # headless browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=options)

        driver.get(pageurl)
        driver.maximize_window()
        time.sleep(2)
        pageSource = driver.page_source
        WebDriverWait(driver, 10).until(EC.title_contains(pageTitle))
        if(driver.title != pageTitle):
            print("Connection Failed")
            return
        soup = BeautifulSoup(pageSource, 'lxml')
        driver.close()
        return soup
    except Exception as e:
        print("Some error occured, error: ", e)
        return
