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
import connection;
# End local imports

# Begin class
class ChatdServer(object):
    # ChatdServer -- Manage chat threads and socket objects to facilitate
    # communication between all clients

    def __init__(self):
        # Takes no arguments, returns new ChatdServer object

        # Initialize server socket
        self.serverSocket = socket.socket();

    def bind(self, port):
        # Binds server socket to all interfaces on given port. Expects UInt16.

        # Bind server to all interfaces
        self.serverSocket.bind(("0.0.0.0",port));

    def open(self):
        # Begins listening for requests. Does not return.

        #TODO: Implement
