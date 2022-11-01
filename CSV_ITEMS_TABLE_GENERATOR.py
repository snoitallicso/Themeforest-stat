import sqlite3
import csv

dbPath = 'E:\_\Sales gathering\exmpl.sqlite'
csvPath = 'E:\_\Sales gathering\comparison_table.csv'

#tables = [2833226]
#tables = [2833226,5871901]
#tables = [2833226,5871901,7758048]
#tables = [2833226,5871901,7758048,4519990]
#tables = [2833226,5871901,7758048,4519990,5177775,7315054,5489609,11776839,5484319,13373220,4021469]
#tables = [2833226,5871901,7758048,4519990,7315054,5177775,5489609,4363266,5556590,5484319,13373220,4021469,6434280,9228123,9602611,6339019,4091658,4106987,13739153,10860525,16164427,8819050,9545812,11776839,9725864,14740561,14438769,9207399,6776630,13542725,12945398,9553045,11562108,13398377,13304399,14058034,12931855,14881144,5373914,6780226,11989202,6221179,2819356,4260361,13080328,15409157,11099136,11671924,10648488,5247604,7896392,11330434,12537825,10439297,9512331,11400130,15917131,15720624,12473778,13925633,16230780,7920093,253220,11811123,15709244,13987211,12087239,16422281,15752549,15780546,13570398,15791151,14493994,9865647,10802918,14051111,16061685,17870799,16912793,12650481,17238971,15801051,7646339,15896734,16869357,17465118,8012838,17338706,14906749,15761106,17672485,10591107,9694847,17795788,17268942,15175900,11820082,17336192,13244840,16510989,13708923,17268951,11413730,19016121,3840053,19133384,19054317,9691007,5443578,9693644,16999050,16202433,18276186,13905328,7902937,15860489,14221636,4287447,18332889,19196010,19075153,18968307,16524248,11118909,15709444,13439786,15113981,15365040,15043746,16750820,15550221,12649286,15730392,16677956,16596434,11987314,3231798,15939582,5235877,9646105,14342350,15884091,16430770,18151772,18081003,18072368,7163563,15148004,17104538,16897309,4087140,17990371]
tables = [2833226,5871901,7758048,4519990,7315054,5177775,5489609,4363266,5556590,5484319,13373220,4021469,6434280,9228123,9602611,6339019,4091658,4106987,13739153,10860525,16164427,8819050,9545812,11776839,9725864,14740561,14438769,9207399,6776630,13542725,12945398,9553045,11562108,13398377,13304399,14058034,12931855,14881144,5373914,6780226,11989202,6221179,2819356,4260361,13080328,15409157,11099136,11671924,10648488,5247604,7896392,11330434,12537825,10439297,9512331,11400130,15917131,15720624,12473778,13925633,16230780,7920093,253220,11811123]

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

	csvWriter = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')

	#TODO: generator first row (size, names etc)
	csvWriter.writerow(firstCsvRowArray)
	
	for row in c.execute(queryGetTables):

		#print(row)
		csvWriter.writerow(row)


# Save (commit) the changes
#conn.commit()

# We can also close the cursor if we are done with it
#c.close()
