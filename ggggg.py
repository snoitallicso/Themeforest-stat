import hashlib
#import sqlite3

#c = sqlite3.connect("D:\WORKSPACE\STATISTICS\Sales gathering\example.sqlite").cursor()

#c.execute()

arr = [1,2,3,4]
arrLen = len(arr)

invertConcatList = []

for item in range(0,arrLen):

        for sec_item in range(0,arrLen):

                invConc = str(arr[sec_item]) + "," + str(arr[item])
                normConc = str(arr[item]) + "," + str(arr[sec_item])
                
                ##print 'invConc:',invConc,'normConc:',normConc

                if arr[item] != arr[sec_item]:

                        if normConc in invertConcatList:
                                
                                #print 'invConc in invertConcatList'
                                #print arr[item],arr[sec_item]
                                1+1

                        else:

                                print arr[item],arr[sec_item]

                                invertConcatList.append(invConc)
                                #print 'invertConcatList:',invertConcatList
                        
                else:
                        1+1
                        #print 'keys duplicates'


#print hashlib.md5(b'1').hexdigest()

#CREATE TABLE `correlations_2015plus` (`item1` INT NULL,`item2` INT NULL)