from bs4 import BeautifulSoup
import sqlite3
from PREFS import dbPath, tbl_Topweek_Log



###### THIS FILE PARSE HTML FILES INTO BIG LOG TABLE (__topweek_log) THAT INCLUDE DATA WITH TOP SELLING THEMES OF ALL PERIODS
###### BEFORE USING PREPARE index's.html pages and change path folder
###### THIS LOG TABLE IS START POINT FOR FUTHER PROCESSING
###### 1 FILE



######CONNECT TO DB
conn = sqlite3.connect(dbPath)
c = conn.cursor()

######CREATE table for logs
c.execute('''CREATE TABLE IF NOT EXISTS "main"."'''+tbl_Topweek_Log+'''" ("Sales_period" TEXT, "Item_title" VARCHAR, "Item_id" INTEGER, "Price" INTEGER, "Sales")''')

#GOAL: get webpage date period (end week for top sellers)

#TODO: auto docs len counter #376
for pagenum in range(2,382):

	webpage = BeautifulSoup(open("C:\Users\me\Desktop\!!!2\index (" +str(pagenum)+ ").html"), "html.parser")
	rawdatetitle = webpage.find_all("h1", class_="t-heading")[0]
	dateString = rawdatetitle.text[22:30] #[08/06/14]
	dateString = "20"+dateString[6:8]+"-"+dateString[3:5]+"-"+dateString[0:2] #[08/06/14 to 2014-06-08]

# #GOAL: get Sales, Item id and Name for each item presented on the page
	weeklyTopHTML = webpage.find_all("ul", class_="item-grid")[0]

	##get items raw array
	itemsRawHTML = weeklyTopHTML.find_all("li", class_="js-google-analytics__list-event-container")

	print "page number: "+ str(pagenum) + " Top week items: "+ str(len(itemsRawHTML)) + " Week: " + str(dateString)

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
