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
import json;
# End system imports

# Begin local imports
import src.crypt;
from src.sender import Sender;
# End local imports

# Static vars
QUIT_MSGS = [
    ":q",
    ":d",
    ":quit",
    ":disconnect"
];

# Begin class
class Connection(threading.Thread):
    # Connection -- Maintains and manages connections with client classes.
    # Runs a thread for each client.

    def __init__(self, client, user, key, server):
        # Connection(client) takes a client socket and an RSA public key
        # and returns a Connection object

        # Save client so we can communicate with it later
        self.client = client;

        # Save username so we can utilize it later
        self.user = user

        # Initialize RSA public key
        self.key = key;

        # Save server obj for reference
        self.serv = server;

        # Create helper thread for message transmission, so the receiver doesn't
        # block while waiting to send
        self.sender = Sender(self.serv);

        # Run super.init
        threading.Thread.__init__(self);

    def run(self):
        # Implement listener

        jsonDecoder = json.JSONDecoder();

        while True:
            # Block until data received
            data = self.client.recv(4096);

            # Decrypt
            #data = crypt.decrypt(data);

            # When received, decode into JSON string
            jsonCode = data.decode('utf-8');

            # Decode JSON string into dictionary
            contents = jsonDecoder.decode(jsonCode);
            
            # First, check to see if message is a quit command
            if contents['message'] in QUIT_MSGS:
                # If so, break the loop.
                break;

            self.sender = Sender(self.serv);
            self.sender.send_message(jsonCode);

        # End loop

        # Close connection
        self.client.close();

    def send_message(self, message):
        # Sends `message`, a JSON string, to the client.

        # Encode
        encoded = message.encode('utf-8');
        
        # Encrypt
        #encoded = crypt.encrypt(encoded);

        # Send encrypted message
        self.client.sendall(encoded);
