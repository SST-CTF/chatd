#!/usr/bin/env python3

#
# main.py
#
# Created by Stephen Brimhall on 1/22/17
# Copyright (c) SST CTF and Stephen Brimhall. All Rights Reserved.
#
# Implements the primary server of the SST CTF chat network system.
# This file contains the startup for the server.
#

# Begin module imports
import socket;
import sys;
import os;
# End module imports

# Begin user imports
#import src.RequestHandler
# End user imports

# main

# Create socket
sock = socket.socket();

# Bind socket to localhost port 
sock.bind(("localhost",20039));

newsock,_ = sock.accept();


