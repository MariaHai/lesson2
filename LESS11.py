from bs4 import BeautifulSoup
import requests
response = requests.get("https://uaspeedfilms.club")
f = open("film.txt" , "a+")
if response.status_code == 200:
    soup = BeautifulSoup(response.text , features="html.parser")
    name_list_soup = soup.find_all("strong", {"class":"shortnew-main-item-title"})
    year_list_soup = soup.find_all("a", {"href":"/filmy-ta-serialy-2022-iaki-vzhe-vyishly.html"})
    #year_list = soup.find_all("p",{"class": "sc-1eb5slv-0 iworPT"})
    # res = soup_list[0].find("span")
    # print(res.text)
    nameList = []
    yearList = []
    for elementName in name_list_soup :
        nameList.append(str(elementName.text))
    lenList = len (nameList)
    print(lenList)
    l = [str(i) for i in range(0,lenList)]
    for elementYear in year_list_soup :
        yearList.append(str(elementYear.text))
    lenList = len(yearList)
    print(lenList)
    l = [str(i) for i in range(0, lenList)]
    for i in range(0,lenList):
        str = l[i]+nameList[i]+"\n"
        f.write(str)
        print(i,")",nameList[i], yearList[i], "I")





#<div class="sc-131di3y-0 cLgOOr"><a href="/currencies/ethereum/markets/" class="cmc-link"><span>$1,669.14</span></a></div>
#<a href="/filmy-ta-serialy-2022-iaki-vzhe-vyishly.html"><li>2022</li></a>