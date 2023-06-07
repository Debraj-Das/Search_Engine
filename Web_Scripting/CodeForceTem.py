import page as pg

problemUrl = "https://codeforces.com/problemset"
order = ["BY_RATING_ASC","BY_RATING_DESC","BY_SOLVED_DESC", "BY_SOLVED_ASC"]

soup = pg.webPage(problemUrl+"?order="+order[0])


# find the number of pages
pages = soup.find('div', class_="pagination")
pages = pages.find_all('li')
pages = pages[-2].text
pages = int(pages)


print("Total pages:", pages)

for index in range(1 , pages+1):
    newsoup = pg.webPage(problemUrl+"/page/"+str(index)+"?order="+order[0])
    s = newsoup.findAll('tr')

    for i in (s):
        name = i.find(attrs={'style': 'float: left;'})
        tag = i.find(class_="notice")
        if (name == None and tag == None):
            continue

        qurl = i.find('a')['href']
        diff = i.find(class_="ProblemRating").text
        name = ((name.text).replace('\n', ''))[1:]

        print(name,qurl, tag.text,diff, sep=' ')

def fetch():
    pass


def get():
    pass




if "__name__"=="__main__":
    pass







# s = soup.findAll('tr')

# for index, i in enumerate(s):
#     name = i.find(attrs={'style': 'float: left;'})
#     tag = i.find(class_="notice")
#     if (name == None and tag == None):
#         continue

#     qurl = i.find('a')['href']
#     diff = i.find(class_="ProblemRating").text
#     name = ((name.text).replace('\n', ''))[1:]

#     print(index, ') ', name,qurl, tag.text,diff, sep=' ')
