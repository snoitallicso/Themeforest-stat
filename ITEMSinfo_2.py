from bs4 import BeautifulSoup
import csv

#GOAL: get webpage date period (end week for top sellers)

for pagenum in range(2,376):

	webpage = BeautifulSoup(open("C:\Users\me\Desktop\!!!2\index (" +str(pagenum)+ ").html"))
	rawdatetitle = webpage.find_all("h1", class_="t-heading")[0]
	dateString = rawdatetitle.text[22:30]
	###print dateString

	#GOAL: get Sales, Item id and Name for each item presented on the page
	with open('D:\WORKSPACE\STATISTICS\Sales gathering\Python scripts\eggs.csv', 'ab') as f:
		spamWriter = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=';')

		weeklyTopHTML = webpage.find_all("ul", class_="item-grid")[0]

		##get items raw array
		itemsRawHTML = weeklyTopHTML.find_all("li", class_="js-google-analytics__list-event-container")

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


			print dateString
			print itemTitle
			print dataItemId
			print dataItemCost
			print saleCount
		
			spamWriter.writerow([str(dateString),itemTitle,str(dataItemId),str(dataItemCost),str(saleCount)])
		
		#spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
# + [itemTitle] + [dataItemId] + [dataItemCost] + [saleCount]

###GET FROM JSON
###q['position']
###q = json.loads('{"id":2833226,"name":"Avada | Responsive Multi-Purpose Theme","brand":"ThemeFusion","category":"themeforest.net/category/wordpress/corporate","position":1,"list":"Weekly Top Sellers"}')
