#!/usr/bin/env python3

#
# connection.py
# Created by Stephen Brimhall on 1/23/17
# Copyright (c) SST CTF and Stephen Brimhall. All Rights Reserved.
#
# Implements the Connection class, which runs as a separate thread to handle
# client programs
#

# Begin system imports
import socket;
import threading;
# End system imports

# Begin class
class Connection(threading.Thread):
    # Connection -- Maintains and manages connections with client classes.
    # Runs a thread for each client.

    def __init__(self, client, key):
        # Connection(client) takes a client socket and an RSA public key
        # and returns a Connection object

        # Save client so we can communicate with it later
        self.client = client;

        # Initialize message queue
        self.messageQueue = [];

        # Initialize queue lock
        self.messageLock = threading.RLock();


        # Initialize RSA public key
        self.key = key;

    def add_message(self, message):
        # Adds a message to the message queue. Will send after all prior
        # messages have been sent.

        # Aquire lock and add message
        with self.messageLock:
            self.messageQueue.append(message);
            
    def run(self):
        # Implement listener

        # TODO: implement.

        pass;

        #while True:
        #    data = self.client.recv();
