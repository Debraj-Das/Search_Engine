import page as pg


def fetch_every_question(url ):
    pass





def fetch(url , sheet):
    newsoup = pg.webPage(url)
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
        sheet.append([name, qurl, tag, diff])
    return


def get(problemUrl , order):
    soup = pg.webPage(problemUrl+"?order="+order[0])

    # find the number of pages
    pages = soup.find('div', class_="pagination")
    pages = pages.find_all('li')
    pages = pages[-2].text
    pages = int(pages)
    print("Total pages:", pages)
    
    # List to store all the questions
    problemsheet = [["Problem Name", "Problem URL", "Problem Tag", "Difficulty"],]

    # Fetching data from each page
    for index in range(1 , pages+1):
        print(f"\n********Fetching Page {index}********")
        url = problemUrl+"/page/"+str(index)+"?order="+order[0]
        fetch(url, problemsheet)
        print("********Done********")
    
    # All fetched data and now creating excel sheet with the data
    print("*****Done all pages*****")
    print(f"Total {problemsheet.__len__()} questions fetched")
    
    # Now 
    
    
    
    
    return



if __name__ == "__main__":
    problemUrl = "https://codeforces.com/problemset"
    order = ["BY_RATING_ASC","BY_RATING_DESC","BY_SOLVED_DESC", "BY_SOLVED_ASC"]
    get(problemUrl, order)