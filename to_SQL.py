import csv
import MySQLdb

mydb = MySQLdb.connect(Host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()

csv_data = csv.reader(file('file.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO testcsv(names, \
          )' \
          'VALUES("%s", "%s", "%s")', 
          row)
#close the connection to the database.
cursor.close()
print "Done"