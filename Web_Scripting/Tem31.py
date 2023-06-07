from bs4 import BeautifulSoup
import requests
import os


def webPage(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    return soup



def fetch_every_question(url):
    newsoup = webPage(url[1])
    text = newsoup.select_one("#pageContent > div.problemindexholder > div.ttypography > div > div:nth-child(2)").text
    text = text.replace('$', '')
    name = url[0].replace(' ', '_')
    name = name.replace('.', '_')
    
    input = f"{url[0]}\n\n{url[1]}\n\n{url[2]}\n\n{url[3]}\n\n{text}"
    print(input)
    # creating file and writing the input file
    with open(f"{name}.txt", 'w') as f:
        f.write(input)
    
    return




if __name__ == "__main__":
    url = ["Editorial for Two", "https://codeforces.com/problemset/problem/1837/F", ["math","binary number", "implementation"], "1600"]
    fetch_every_question(url)
 