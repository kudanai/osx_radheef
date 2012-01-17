#!/usr/bin/env python

import sqlite3
import csv

csvReader = csv.DictReader(open('radheef.csv','rb'),delimiter="\t",fieldnames=('word','meaning','type'),restval="")

with sqlite3.connect('radheef.sqlite3') as conn:
    cur = conn.cursor()

    #drop the radheef table first, and create a new table
    cur.execute('DROP TABLE IF EXISTS radheef')
    cur.execute('CREATE TABLE radheef (headWord TEXT,wordType TEXT,definition TEXT)')


    #start stuffing the data into the database
    for row in csvReader:
        
        #tuple containign the dictionary entry
        #TODO: cleanup those definitions perhaps?
        dictEntry = (row['word'].strip(),row['type'].strip(),row['meaning'].strip())
        
        #insert the data
        cur.execute('INSERT INTO radheef VALUES (?,?,?)',dictEntry)