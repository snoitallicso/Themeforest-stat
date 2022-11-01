import sqlite3
from PREFS import dbPath, tbl_Topweek_Log, tbl_Themes_List



###### //THIS FILE PARSE HTML FILES INTO BIG LOG TABLE (__topweek_log) THAT INCLUDE DATA WITH TOP SELLING THEMES OF ALL PERIODS
###### //BEFORE USING PREPARE index's.html pages and change path folder
###### //THIS LOG TABLE IS START POINT FOR FUTHER PROCESSING
###### 3 FILE



##TODO: CREATE THEMES LIST TABLE AND
## 		PUT UNIQUE DATA


######CONNECT TO DB
conn = sqlite3.connect(dbPath)
c = conn.cursor()

######CREATE "__themes_list" list table for further big goal: mass creating themes tables
#c.execute('''DROP TABLE "main"."__themes_list"''')
c.execute('''CREATE TABLE "'''+tbl_Themes_List+'''" ("Item_title" VARCHAR, "Item_id" INTEGER UNIQUE, "Price" INTEGER)''')

######MERGE LOG FROM MAIN LOG TABLE "__topweek_log" INTO "__themes_list". THANKS TO UNIQUE
c.execute('''INSERT OR IGNORE
				INTO "main"."'''+tbl_Themes_List+'''"
				SELECT "Item_title", "Item_id", "Price"
				FROM "'''+tbl_Topweek_Log+'''"''')



# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()