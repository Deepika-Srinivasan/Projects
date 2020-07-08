import mysql.connector

mydb = mysql.connector.connect(
  host="mysql2020.c8zaxnpj5b57.us-east-1.rds.amazonaws.com",
  user="mysql2020",
  passwd="mysql2020"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE cloudcruise")

mycursor.execute("USE cloudcruise")

mycursor.execute("CREATE TABLE logs (image_id INT AUTO_INCREMENT,image_name TEXT,image_class TEXT,PRIMARY KEY (image_id))ENGINE=INNODB")

mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)

mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)