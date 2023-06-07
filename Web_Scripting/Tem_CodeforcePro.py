from bs4 import BeautifulSoup
import requests
import os


def webPage(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    return soup


def fetch_every_question(url):
    try:
        try:
            print(f"\nFetching {url[0]}")
        except:
            url[0] = ''.join(letter for letter in url[0] if letter.isalnum())
            print(f"\nFetching {url[0]}")
            
        
        newsoup = webPage(url[1])
        text = newsoup.select_one("#pageContent > div.problemindexholder > div.ttypography > div > div:nth-child(2)").text
        text = text.replace('$', '')
        name = url[0].replace(' ', '')
        
        input = f"{url[0]}\n\n{url[1]}\n\n{url[2]}\n\n{url[3]}\n\n{text}"
        # creating file and writing the input file
        try:
            with open(f"{name}.txt", 'w') as f:
                f.write(input)
        except:
            input = ''.join(letter for letter in input if (letter.isalnum() or letter == ' ' or letter == '\n'))
            with open(f"{name}.txt", 'w') as f:
                f.write(input)
        
        print(f"Done {url[0]}")
    except Exception as e:
        print("Error in fetching question:")
        print("Due to ", e)
    
    return


def fetch(url , problemsheet):
    newsoup = webPage(url)
    s = newsoup.findAll('tr')
    for i in (s):
        # Question Name
        name = i.find(attrs={'style': 'float: left;'})
        if(name == None): continue
        name = ((name.text).replace('\n', ''))[1:]
            
        # Question Tag
        tag = i.find(class_="notice")
        if (tag != None):
            tag = tag.text
        else:
            tag = ''
        
        # Question URL
        qurl = i.find('a')['href']
        qurl = "https://codeforces.com"+qurl
        
        # Difficulty
        diff = i.find(class_="ProblemRating").text
        diff = int(diff)
        
        # append to sheet
        problemsheet.append([name, qurl, tag, diff])
    return


def get(problemUrl , order):
    soup = webPage(problemUrl+"?order="+order[0])

    # find the number of pages
    pages = soup.find('div', class_="pagination")
    pages = pages.find_all('li')
    pages = pages[-2].text
    pages = int(pages)
    print("Total pages:", pages)
    
    # List to store all the questions
    problemsheet = []

    # Fetching data from each page
    for index in range(1 , pages+1):
        print(f"\n********Fetching Page {index}********")
        url = problemUrl+"/page/"+str(index)+"?order="+order[0]
        fetch(url, problemsheet)
        print("********Done********")
    
    # All fetched data and now creating excel sheet with the data
    print("*****Done All Question Pages Url*****")
    lenth = problemsheet.__len__()
    print(f"Total {lenth} questions fetched")
    
    # Now fetching data from each question and storing it in text files in problem folder
    
    try:
        os.mkdir("Problems")
        os.chdir("Problems")
    except:
        print("Folder already exists")
        os.mkdir("New Problems folder")
        os.chdir("New Problems folder")
    
    for i ,problemUrl in enumerate(problemsheet):
        print(f"\n*******Fetching Question {i+1} in {lenth}*******")
        fetch_every_question(problemUrl)
    
    print("\n\n\t*******Done All Questions*******")
    
    
    return


if __name__ == "__main__":
    problemUrl = "https://codeforces.com/problemset"
    order = ["BY_RATING_ASC","BY_RATING_DESC","BY_SOLVED_DESC", "BY_SOLVED_ASC"]
    get(problemUrl, order)
    
