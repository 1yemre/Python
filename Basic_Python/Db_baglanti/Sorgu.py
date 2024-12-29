import sqlite3

connection=sqlite3.connect("deneme.db")
cursor=connection.cursor()

sql="INSERT INTO  genres(name) VALUES ('MACERA')"
cursor.execute(sql)

connection.commit() #çalıştırdık


#cursor.execute("select * from customers where city='oslo' ")
#customers=cursor.fetchall()#çoklu kayit
# customers=cursor.fetchone()  # tek kayit





# for customer in customers:
#     print(customer[1]+ " "+customer[2])


connection.close()
print("db okey")

