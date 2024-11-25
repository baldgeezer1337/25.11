import sqlite3

conn=sqlite3.connect('test.db')

"""print('Datubāze ir izveidota!')
conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY  NOT NULL,
             NAME      TEXT       NOT NULL,
             AGE       INT        NOT NULL,
             ADRESS    CHAR(50),
             SALARY    REAL);''')
print('Tabula ir izveidota!')"""

"""conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print('Kopeju izmainu skaits:', conn.total_changes)"""

"""conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY)\
             VALUES(1,'Paul',32,'California', 20000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY)\
             VALUES(2,'Alex',25,'Latvia', 15000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY)\
             VALUES(3,'Teddy',23,'Norway', 20000.00)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY)\
             VALUES(4,'Mark',25,'Germany', 65000.00)");

conn.commit()"""

conn.execute('DELETE from COMPANY where ID=2;')
conn.commit()
print('Dzestu vienibu skaits:', conn.total_changes)

cursor=conn.execute("SELECT * from COMPANY")
for ieraksts in cursor:
    print("ID= ", ieraksts[0])
    print("NAME= ", ieraksts[1])
    print("AGE= ", ieraksts[2])
    print("ADRESS= ", ieraksts[3])
    print("SALARY= ", ieraksts[4],"\n")

print('Dati ir veiksmigi dzesti')
#print('Ieraksti ir izveidoti')
conn.close()