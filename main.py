#!/usr/bin/env python

import os
import pathlib
import re
import sqlite3
import sys

contact = "+55 00 0000 0000"

chat = "/path/to/chat.txt"
database = "/path/to/sqlite.db"

day = None
month = None
year = None
hour = None
minute = None
sender = None
message = None

con = sqlite3.connect(database)
cur = con.cursor()
cur.execute("CREATE TABLE conversations (id INTEGER PRIMARY KEY AUTOINCREMENT, contact TEXT NOT NULL, date TEXT NOT NULL, time TEXT NOT NULL, sender TEXT NOT NULL, message TEXT);")

with open(chat) as file:
    for line in file:
        pattern = re.compile("^([0-9]{1,2})/([0-9]{1,2})/([0-9]{2,4}) ([0-9]{1,2}):([0-9]{2}) - ([^:]+): (.*)$")
        result = pattern.match(line)
        if result:
            if day and month and year and hour and minute and sender:
                date = f"{year}-{month}-{day}"
                time= f"{hour}:{minute}"
                cur.execute("INSERT INTO conversations (contact, date, time, sender, message) VALUES (?, ?, ?, ?, ?);", (contact, date, time, sender, message))
                con.commit()
            day = result.group(1)
            month = result.group(2)
            year = result.group(3)
            hour = result.group(4)
            minute = result.group(5)
            sender = result.group(6)
            message = result.group(7)
        else:
            message = message + "\n" + line.rstrip()

if day and month and year and hour and minute and sender:
    date = f"{year}-{month}-{day}"
    time= f"{hour}:{minute}"
    cur.execute("INSERT INTO conversations (contact, date, time, sender, message) VALUES (?, ?, ?, ?, ?);", (contact, date, time, sender, message))
    con.commit()
