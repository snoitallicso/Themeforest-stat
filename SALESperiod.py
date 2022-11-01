from bs4 import BeautifulSoup

webpage = BeautifulSoup(open("C:\Users\me\Desktop\!!!2\index (81).html"))
rawdatetitle = webpage.find_all("h1", class_="t-heading")[0]
dateString = rawdatetitle.text[22:30]
print dateString