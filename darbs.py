import sqlite3

conn=sqlite3.connect('biblioteka.db')

"""print('Datubāze ir izveidota!')
conn.execute('''CREATE TABLE GRAMATAS
             (GRAMATAS_ID INT PRIMARY KEY  NOT NULL,
             NOSAUKUMS      TEXT       NOT NULL,
             GADS       INT        NOT NULL,
             AUTORA_ID    INT NOT NULL);''')
conn.close()

conn.execute('''CREATE TABLE AUTORS
             (AUTORA_ID INT PRIMARY KEY  NOT NULL,
             VARDS      TEXT       NOT NULL,
             UZVARDS       TEXT        NOT NULL);''')
print('Tabula ir izveidota!')"""

"""conn.execute("INSERT INTO GRAMATAS (GRAMATAS_ID,NOSAUKUMS,GADS,AUTORA_ID)\
             VALUES(1,'Kolobok',1986,50)");

conn.execute("INSERT INTO GRAMATAS (GRAMATAS_ID,NOSAUKUMS,GADS,AUTORA_ID)\
             VALUES(2,'Dezhavju',2019,51)");

conn.execute("INSERT INTO GRAMATAS (GRAMATAS_ID,NOSAUKUMS,GADS,AUTORA_ID)\
             VALUES(3,'White Noise',2001,52)");


conn.execute("INSERT INTO AUTORS (AUTORA_ID,VARDS,UZVARDS)\
             VALUES(50,'Igors','Valambaevs')");

conn.execute("INSERT INTO AUTORS (AUTORA_ID,VARDS,UZVARDS)\
             VALUES(51,'Oleg','Netrureps')");

conn.execute("INSERT INTO AUTORS (AUTORA_ID,VARDS,UZVARDS)\
             VALUES(52,'Aphex','Twins')");"""

cursor=conn.execute("SELECT * from GRAMATAS")
for ieraksts in cursor:
    print("NOSAUKUMS= ", ieraksts[1])
    print("GADS= ", ieraksts[2],"\n")


conn.commit()

conn.close()