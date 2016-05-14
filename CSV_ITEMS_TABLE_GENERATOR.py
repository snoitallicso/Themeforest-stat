import sqlite3
import csv

dbPath = 'E:\Sales gathering\exmpl.sqlite'
csvPath = 'E:\Sales gathering\comparison_table.csv'

#tables = [2833226]
#tables = [2833226,5871901]
#tables = [2833226,5871901,7758048]
#tables = [2833226,5871901,7758048,4519990]
#tables = [2833226,5871901,7758048,4519990,5177775,7315054,5489609,11776839,5484319,13373220,4021469]
tables = [2833226,5871901,4519990,7758048,7315054,5177775,4363266,5484319,5489609,4021469,5556590,13373220,11776839,9228123,6339019,10860525,9545812,6434280,4106987,12945398,2819356,8819050,9725864,13398377,9207399,4091658,6776630,6221179,9553045,13304399,9602611,13925633,6780226,4260361,13542725,11099136,11562108,14058034,8012838,13080328,10648488,5373914,253220,7920093,11118909,13708923,9512331,12931855,11811123,7896392,3231798,11330434,13460357,11671924,9210971,11989202]

######CONNECT TO DB
conn = sqlite3.connect(dbPath)
c = conn.cursor()

titles = []
firstCsvRowArray = ['Sales period']

for id in range(0, len(tables)):
	qGt = c.execute('SELECT `Item_title` FROM `__themes_list` WHERE `Item_id` = '+str(tables[id])).fetchone()[0]
	titles.append(qGt)
	
	#PUSH TITLES
	firstCsvRowArray.append(titles[id].encode('utf-8','ignore'))

	print titles[id]
	print titles[id].encode('utf-8')
	print titles[id].encode('utf-8','ignore')


query_concat_FromJoinedIds = ''	#no join any item
query_concat_OnJoinPeriods = '' #ON() is odd syntax for one item

if(len(tables) <= 1):

	#query_concat_SelectIds = ', `' + str(tables[0]) + '`.`Sales` as `' + str(titles[0]) + '`'
	query_concat_SelectIds = ''
	query_concat_FromJoinedIds = ''	#no join any item
	query_concat_OnJoinPeriods = '' #ON() is odd syntax for one item
	
else:

	query_concat_SelectIds = ''
	query_concat_OnJoinPeriods = ' ON ('
	
	for id in range(1, len(tables)):
		
		query_concat_SelectIds += ', `' + str(tables[id]) + '`.`Sales` as `' + titles[id] + '`'
		query_concat_FromJoinedIds += ' JOIN `'+ str(tables[id]) +'`'
		
		if(len(tables) >= 2):
			if(id != len(tables)-1):
				query_concat_OnJoinPeriods += '`' + str(tables[id]) +'`.`Sales_period` = `' + str(tables[0]) + '`.`Sales_period` AND '
			else:
				query_concat_OnJoinPeriods += '`' + str(tables[id]) +'`.`Sales_period` = `' + str(tables[0]) + '`.`Sales_period`)'
		else:
			query_concat_OnJoinPeriods += '`' + str(tables[id]) +'`.`Sales_period` = `' + str(tables[0]) + '`.`Sales_period`)'


#print 'SELECT `'+str(tables[0])+'`.`Sales_period`, `'+str(tables[0])+'`.`Sales` as `' + str(titles[0]) + '`' + query_concat_SelectIds + ' FROM `' + str(tables[0]) + '`' + query_concat_FromJoinedIds + query_concat_OnJoinPeriods + ' ORDER BY `' + str(tables[0]) + '`.`Sales_period` ASC'
		
#GENERATED sql
queryGetTables = 'SELECT `'+str(tables[0])+'`.`Sales_period`, `'+str(tables[0])+'`.`Sales` as `' + str(titles[0]) + '`' + query_concat_SelectIds + ' FROM `' + str(tables[0]) + '`' + query_concat_FromJoinedIds + query_concat_OnJoinPeriods + ' ORDER BY `' + str(tables[0]) + '`.`Sales_period` ASC'

#TODO: rewrite file on each operation
with open(csvPath, 'ab') as f:

	csvWriter = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=';')

	#TODO: generator first row (size, names etc)
	csvWriter.writerow(firstCsvRowArray)
	
	for row in c.execute(queryGetTables):

		#print(row)
		csvWriter.writerow(row)


# Save (commit) the changes
#conn.commit()

# We can also close the cursor if we are done with it
#c.close()
