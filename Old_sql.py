# import sqlite3
import sqlalchemy
import csv
import db

print(db.var)
exit()

# connect to database
# db = sqlite3.connect('test.db')
#engine = sqlalchemy.create_engine('sqlite:///database.db', echo=True, echo_pool='debug')
engine = sqlalchemy.create_engine('sqlite:///database.db')

# kursori jonka kautta lähetetään sql käskyjä
# cur = db.cursor()  # Välilyönnit ei ole pakolliset muttaa näyttää paremmalta

#engine.execute(""Create table if not exists users (name text, email text)"")
#engine.execute("Create table if not exists links (url text, email text)")
#engine.execute("Create table if not exists tax (company text, tax_paid text)")

#create trasaction
con = engine.connect()

#trasaction
trans = con.begin()
con.execute("Create table if not exists tax (company text, tax_paid text)")


#cur.execute("Create table if not exists users (name text, email text)")
#cur.execute("Create table if not exists links (url text, email text)")
#cur.execute("Create table if not exists tax (company text, tax_paid text)")

#db.commit()
#db.close()
#exit()

#cur.execute("insert into users values ('Jari', 'jari@jari.fi')")
#cur.execute("insert into links  values ('https://Jari.fi', 'jari@jari.fi')")
#cur.execute("insert into links  tax ('https://Jari.fi', 'jari@jari.fi')")

#for row in cur.execute('select * from users'):
#    print(row[0])
#    for link in cur.execute('select url from links where email=?', (row[1],)):
#        print(link[0])
    

with open('data.csv', 'r', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    line = 0
    for row in reader:
        if line != 0:
            #print('Inserting line {}'.format(line))
            con.execute("insert into tax values (?, ?)", (row[2], row[5]))
        line += 1


trans.commit()
con.close()
#db.commit()
#db.close()