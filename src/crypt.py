#!/usr/bin/env python3

#
# crypt.py
# Created by Stephen Brimhall on 1/23/17
# Copyright (c) SST CTF and Stephen Brimhall. All Rights Reserved.
#
# crypt.py contains utility functions for encryption and decryption of messages.
#

# Begin system imports
## Import cryptography library here once ready
# End system imports

def encrypt(string, key=None):
    # encrypt() takes a string and an optional key, returning `string` encrypted
    # with RSA key `key`. `key` defaults to none, meaning no encryption
    # is performed.

    if key == None:
        return string;
    else:
        # Do something. For now, return the string.
        return string;

def decrypt(string, key=None):
    # decrypt() takes a string and an optional key, returning `string` decrypted
    # with RSA key `key`. `key` defaults to none, meaning string should be
    # assumed to contain no encryption and therefore no action need be taken.

    if key == None:
        return string;
    else:
        # Do something. For now, return the string.
        return string;
