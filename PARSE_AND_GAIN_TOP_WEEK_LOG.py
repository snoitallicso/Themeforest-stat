from bs4 import BeautifulSoup
import sqlite3
from PREFS import dbPath, pagesPath, tbl_Topweek_Log
from datetime import datetime,timedelta
import os

#Py2:
from urlparse import urlparse,parse_qs
#Py3:
#from urllib.parse import urlparse,parse_qs


###### THIS FILE PARSE HTML FILES INTO BIG LOG TABLE (__topweek_log) THAT INCLUDE DATA WITH TOP SELLING THEMES OF ALL PERIODS
###### BEFORE USING PREPARE index's.html pages and change path folder
###### THIS LOG TABLE IS START POINT FOR FUTHER PROCESSING
###### 1 FILE



######CONNECT TO DB
if os.path.exists(dbPath):
	print("Database is exist!")
	os.unlink(dbPath)
	print("Removed")
	
conn = sqlite3.connect(dbPath)
c = conn.cursor()

######CREATE table for logs
c.execute('''CREATE TABLE IF NOT EXISTS "main"."'''+tbl_Topweek_Log+'''" ("Sales_period" TEXT, "Item_title" VARCHAR, "Item_id" INTEGER, "Price" INTEGER, "Sales")''')

for page in os.listdir(pagesPath):

	webpage = BeautifulSoup(open( pagesPath + "/" + page), "html.parser")
	prevWeekUrl = webpage.find("div", class_="week-switcher").a.get("href")

	prevWeekUrl_parsed =urlparse(prevWeekUrl)
	prevWeekQuery =prevWeekUrl_parsed.query
	prevWeekDictDate =parse_qs(prevWeekQuery)

	nextWeekDate = datetime(
			int(prevWeekDictDate["year"][0]),
			int(prevWeekDictDate["month"][0]),
			int(prevWeekDictDate["day"][0])) + timedelta(days=7)

	dateString = nextWeekDate.date()

# #GOAL: get Sales, Item id and Name for each item presented on the page
	weeklyTopHTML = webpage.find_all("ul", class_="item-grid")[0]

	##get items raw array
	itemsRawHTML = weeklyTopHTML.find_all("li", class_="js-google-analytics__list-event-container")

#	print "page number: "+ str(pagenum) + " Top week items: "+ str(len(itemsRawHTML)) + " Week: " + str(dateString)

	for num in range(0, len(itemsRawHTML)):
				
		itemHtmlLi = itemsRawHTML[num]
		
		##item-id
		dataItemId = itemHtmlLi['data-item-id']
		##sales by this period
		dataItemCost = itemHtmlLi.img['data-item-cost']
		saleCount = itemHtmlLi.find_all('small', class_='sale-count')[0]
		saleCount = saleCount.text.replace(' Sales','')
		#itemTitle = itemHtmlLi.img['title']
		itemTitle = itemHtmlLi.img['data-item-name'].encode('utf8')
	
		# Insert into __topweek_log row with some item log
		c.execute('''INSERT INTO "main"."'''+tbl_Topweek_Log+'''" values ("'''+str(dateString)+'''","'''+str(itemTitle)+'''","'''+str(dataItemId)+'''","'''+str(dataItemCost)+'''","'''+str(saleCount)+'''")''')

# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()
