import sqlite3
from PREFS import dbPath, tbl_Topweek_Log, tbl_Fill_Daterange


###### //THIS FILE PARSE HTML FILES INTO BIG LOG TABLE (__topweek_log) THAT INCLUDE DATA WITH TOP SELLING THEMES OF ALL PERIODS
###### //BEFORE USING PREPARE index's.html pages and change path folder
###### //THIS LOG TABLE IS START POINT FOR FUTHER PROCESSING
###### 2 FILE



######CONNECT TO DB
conn = sqlite3.connect(dbPath)
c = conn.cursor()

######CREATE table for date rows each is unique because we set UNIQUE
c.execute('''CREATE TABLE IF NOT EXISTS "main"."'''+tbl_Fill_Daterange+'''" ("Sales_period" TEXT UNIQUE, "Sales" DEFAULT (null))''')

######PUT _ALL_ ROWS FROM COMMON LOGS INTO DATE ROWS TABLE (IT IS SELF-SORTED CAUSE UNIQUE)
c.execute('''INSERT OR IGNORE
				INTO "main"."'''+tbl_Fill_Daterange+'''"
				SELECT "Sales_period", ("null")
				FROM "'''+tbl_Topweek_Log+'''"''')

# Save (commit) the changes
conn.commit()

# We can also close the cursor if we are done with it
c.close()