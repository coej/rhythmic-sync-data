#!/usr/bin/python

#from __future__ import print_function
import os, csv #, re

path = os.path.join(os.getcwd(), 'data_csv_cleaned')

allfiles = os.listdir(path)
csvfiles = [os.path.join(path, f) 
            for f in list(allfiles) 
            if os.path.splitext(f)[1]==".csv"]


def get_file_data(path):
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

#for f in csvfiles:
#    get_file_data(f)
#    break


import psycopg2

#try:
#    conn = psycopg2.connect("dbname='sync_db' user='script_user' host='localhost' password='some_pass'")
#    print conn
#except:
#    print "I am unable to connect to the database"


try:
    conn = psycopg2.connect("dbname='sync_db' user='sync_user'"
                            " host='localhost' password='some_passXX'")
    cur = conn.cursor()
    #cur.execute("select * from participant")
    #rows = cur.fetchall()
    #print rows
    # This works even when the password is incorrect: why?
    # does it have something to do with the script running under
    # the root user?
except psycopg2.ProgrammingError as e:
    raise
except psycopg2.OperationalError as e:
    raise


class ex_fetch:
    def __init__(self, cursor):
        self.cursor = cursor
    def __call__(self, sql):
        self.cursor.execute(sql)
        return cur.fetchall()

# f = ex_fetch(cur)
# print f("select * from participant")

with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        

