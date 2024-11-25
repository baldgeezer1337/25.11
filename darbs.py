import sqlite3

conn=sqlite3.connect('biblioteka.db')

"""print('Datubāze ir izveidota!')
conn.execute('''CREATE TABLE GRAMATAS
             (GRAMATAS_ID INT PRIMARY KEY  NOT NULL,
             NOSAUKUMS      TEXT       NOT NULL,
             GADS       INT        NOT NULL,
             AUTORA_ID    INT NOT NULL);''')
conn.close()"""

conn.execute('''CREATE TABLE AUTORS
             (AUTORA_ID INT PRIMARY KEY  NOT NULL,
             VARDS      TEXT       NOT NULL,
             UZVARDS       TEXT        NOT NULL);''')
print('Tabula ir izveidota!')

conn.close()