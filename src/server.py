#!/usr/bin/env python3

#
# server.py
# Created by Stephen Brimhall on 1/23/17
# Copyright (c) SST CTF and Stephen Brimhall. All Rights Reserved
#
# This file implements the `server` class for the chatd instant messaging system

# Begin system imports
import sys;
import os;
import socket;
import threading;
# End system imports

# Begin local imports
from src.connection import Connection as Client;
from src.queue import Queue as MessageQueue;
# End local imports

# Begin class
class ChatdServer(object):
    # ChatdServer -- Manage chat threads and socket objects to facilitate
    # communication between all clients

    def __init__(self):
        # Takes no arguments, returns new ChatdServer object

        # Initialize server socket
        self.serverSocket = socket.socket();

        # Initialize client list
        self.clients = [];

        # Initialize client list lock
        self.clientLock = threading.RLock();

        # Initialize global message queue
        self.globalMessageQueue = MessageQueue();

    def bind(self, port):
        # Binds server socket to all interfaces on given port. Expects UInt16.

        # Bind server to all interfaces
        self.serverSocket.bind(("0.0.0.0",port));

    def send_message(self, message):
        # Sends `message` to all connected clients.

        # Lock client list so we can safely iterate.
        with self.clientLock:
            # Begin iterating over the client list
            for client in self.clients:
                # Make sure client is alive before sending so we don't trigger
                # an exception
                if client.is_alive():
                    # Send message
                    client.send_message(message);

    def start(self):
        # Begins listening for requests. Does not return.

        #TODO: Implement

        self.serverSocket.listen();

        while True:
            client = self.serverSocket.accept()[0];

            # Retrieve username
            uname = client.recv(4096);

            # Retrieve pubkey
            pubkey = client.recv(4096);

            # Convert bytes to string
            uname = uname.decode('utf-8').strip();
            pubkey = pubkey.decode('utf-8').strip();

            # Debug print statements
            print(uname,pubkey);

            # Check for user's existence
            if uname == "" or not os.path.isdir("/home/" + uname + "/"):
                # If user doesn't exist, close the connection and continue
                client.send("Err: user not found\0".encode("utf-8"));
                client.close();
                continue;

            # Compare to user's authorized_keys
            with open("/home/" + uname + "/.ssh/authorized_keys",'r') as authKeys:
                # Store contents
                contents = authKeys.read();

            # Split into lines, pubkey should be char-for-char
            lines = contents.splitlines();

            # If given pubkey is in the authorized keys file,
            if pubkey in lines:
                # Print debug statement
                print ("Key for user " + uname + " accepted.");
                # Respond with local public key
                with open("/etc/chatd/keys/id_rsa.pub") as serverKey:
                    client.send(serverKey.read().encode("utf-8"));

                # Create handler class and hand off connection management
                handler = Client(client, uname, pubkey, self);

                # Add new handler to client list
                with self.clientLock:
                    self.clients.append(handler);

                # Run handler thread
                handler.start();
                    

        # End listen loop

    # End start function
