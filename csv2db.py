from db.data import insert, start, stop
import csv

session = start()

with open('data.csv', 'r', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    line = 0
    for row in reader:
        if line != 0:
            #print('Inserting line {}'.format(line))
            insert(row[2], row[5], session)
        line += 1

stop(session)