#!/usr/bin/python3

import socket                                                         # for udp socket
import time                                                           # for the sleep() function
PORT = 1307                                                           # random port number (my birthday)
INTERNAL_IP = "127.0.0.1"                                             # internal l0 ip address
SLEEP_TIME = 60                                                       # sleep time
try:
    fileName = input("please enter the filename (without '.txt') that you wish to send to the database: ")
except NameError:
    print("cannot open file, check your spelling or file directory")
while 1:
    try:
        with open(fileName, "r") as f:                                # open the file in reading and mode
            text = f.read()                                           # assigning f into "text" object
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # open udp socket
            s.sendto(text.encode(), (INTERNAL_IP, PORT))              # sending "text" to server (in binary encode)
            print("your message sent successful to the server!")
            time.sleep(SLEEP_TIME)                                    # sleep for one minute

    except KeyboardInterrupt:
        print("\nTHANK YOU for using our network service!\nBYE BYE")  # in case of CTRL+C
        quit()

    except FileNotFoundError:
        print("cannot open file, check your spelling or file directory")
        fileName = input("please 'filename.txt' that you wish to send to the server:")
