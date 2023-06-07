from bs4 import BeautifulSoup
import requests

def webPage(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    return soup

