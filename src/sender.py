#!/usr/bin/env python3

#
# sender.py
# Created by Stephen Brimhall on 1/23/17
# Copyright (c) SST CTF and Stephen Brimhall. All Rights Reserved.
#
# sender.py contains a thread subclass for sending messages. Each client will
# maintain one which will be run only when sending messages.

# Begin system imports
from threading import Thread;
# End system imports

# Begin local imports
# End local imports

class Sender(Thread):
    # Sender -- Thread for sending messages. Exits when all messages sent.
    # Can be restarted whenever message is needed.

    def __init__(self, server):
        # Takes server object and returns a new Sender

        # Initialize server
        self.serv = server;

        # Initialize message
        self.message = "";

        # Run super init
        Thread.__init__(self);

    def send_message(self, message):
        # Takes a message and starts the thread.
        self.message = message;
        self.start();

    def run(self):
        # Sends messages through server send_message method

        self.serv.send_message(self.message);
