#!/usr/bin/python3

import socket                                                   # for udp socket
import sqlite3                                                  # for SQL database
from datetime import datetime                                   # for current time
PORT = 1307                                                     # random port number (my birthday)
INTERNAL_IP = "127.0.0.1"                                       # internal l0 ip address
BUFFER_SIZE = 1024                                              # max buffer for the incoming message

with sqlite3.connect('stations_reports.sqlite') as connection:  # open or create SQL table DB
    connection.execute("""
    CREATE TABLE IF NOT EXISTS station_status(
        station_id INT,
        last_date TEXT,
        alarm1 INT,
        alarm2 TEXT,
        PRIMARY KEY("station_id")
    );
    """)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        # open udp socket
    s.bind((INTERNAL_IP, PORT))                                 # binding the ip & port
    print("server is now running")
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)                    # receiving data
        data = data.decode()                                    # decode the binary to text
        print("data received!")
        data = data.split()                                     # splitting data to three objects
        station = data[0]                                       # station number
        alarm1 = data[1]                                        # alarm 1
        alarm2 = data[2]                                        # alarm 2
        currentTime = datetime.now()                            # get the current time
        timeString = currentTime.strftime("%Y/%m/%d %H:%M")     # praising the current time to pattern
        connection.execute("""
        INSERT OR REPLACE INTO station_status VALUES
        ( ?, ?, ?, ?)
        """, (station, timeString, alarm1, alarm2))
        connection.commit()                                     # sending all data to the SQL table
