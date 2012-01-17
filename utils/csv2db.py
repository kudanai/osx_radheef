#!/usr/bin/env python

##############################################################################
#
# This is a utility script to import data from radheef.csv to an sqlite3
# database. Future implementations of XML generation routines should use
# the db instead of the csv file.
#
# 2012 - kudanai (http://kudanai.com)
#
##############################################################################


import sqlite3
import csv

#we're assuming that radheef.csv is in here somewhere
#note the csv is actuall tab-delimited

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

## end with. 
## commit changes and close connection
