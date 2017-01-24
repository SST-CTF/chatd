#!/usr/bin/env python3

#
# queue.py
# Created by Stephen Brimhall on 1/23/17
# Copyright (c) SST CTF and Stephen Brimhall. All Rights Reserved.
#
# Implements a simple threadsafe queue object.
#

# Begin system imports
from threading import RLock as Lock;
# End system imports

# Queue class

class Queue(object):
    # Queue -- Simple threadsafe queue (list) data structure

    def __init__(self, array=[]):
        # Returns a new queue with the given input

        # Initialize queue
        self.queue = array;

        # Initialize recursive lock (using RLock because it is thread-specific)
        self.lock = Lock();

