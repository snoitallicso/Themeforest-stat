import sqlite3
from PREFS import dbPath, tbl_Topweek_Log, tbl_Fill_Daterange, tbl_Themes_List




###### //THIS FILE CREATE TABLES __FOR EACH THEME__ IT INCLUDES COLS LIKE "Sales_period", "Sales"
###### 4 FILE



######CONNECT TO 1 DB (main data)
conn1 = sqlite3.connect(dbPath)
c1 = conn1.cursor()


# Get table query
c1.execute("""SELECT * FROM main."""+tbl_Themes_List+"""""")

#cache sql into array
vuka =  c1.fetchall()


#array length
#print len(vuka)


######CONNECT TO 2 DB (themes tables)
conn2 = sqlite3.connect(dbPath)
c2 = conn2.cursor()


#TODO: vuka isnt adequate and significant acronym
for row in vuka:
    print row[0]

    tableId = str(row[1])
    tableName = row[0]

    #####################################################

    # Create tableS in e_themeforest_themes.sqlite database
    #c2.execute('''create table "['''+tableId+'''] '''+tableName+'''" ("Sales_period" TEXT (null) UNIQUE, "Sales" DEFAULT (null))''')
    c2.execute('''create table "'''+tableId+'''" ("Sales_period" TEXT UNIQUE, "Sales" DEFAULT (null))''')


    #####################################################

    # FILL UP THEME WITH AVAILABLE TIME ROWS
    c2.execute('''INSERT INTO "'''+tableId+'''" SELECT "Sales_period", "Sales" FROM "'''+tbl_Topweek_Log+'''" WHERE "Item_id"="'''+tableId+'''"''')

    #####################################################

    # FILL UP THEME TABLE WITH UN-AVAILABLE TIME ROWS
    c2.execute('''INSERT OR IGNORE INTO "'''+tableId+'''" SELECT "Sales_period", "Sales" FROM "'''+tbl_Fill_Daterange+'''"''')

# Save (commit) the changes
conn1.commit()
conn2.commit()

# We can also close the cursor if we are done with it
c1.close()
c2.close()
