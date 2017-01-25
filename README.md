# SST CTF Chat Service

[![Code Climate](https://codeclimate.com/github/SST-CTF/chatd/badges/gpa.svg)](https://codeclimate.com/github/SST-CTF/chatd)
[![Issue Count](https://codeclimate.com/github/SST-CTF/chatd/badges/issue_count.svg)](https://codeclimate.com/github/SST-CTF/chatd)

{GIF of chat system running coming soon.}

## Description
#### What
This is a chat service for the SST CTF server. When complete, it will use RSA keypairs
for data encryption and SCP/SFTP for file transfer, making it quite secure. Users will
log in using their server logon name and the server will verify their identity through
`~/.ssh/authorized_keys`. If they are authorized, the server will allow them to
connect. The client will transmit his/her public key on login to enable secure
communications. This server will respond with its public key to facilitate this secure
communication. This key will be encrypted with the client's public key to help foil
man-in-the-middle attacks.

#### Why
Coming soon.


## Instructions
How to install and run the service, coming soon.


## Connecting to this server
The SST CTF chatd service is designed to be extensible and can work with many different
client implementations. However, there are some requirements to effectively communicate
with the server.

#### Handshake
The handshake with the server (initial connection) begins with the client sending a 
username, immediately followed by a public key. The server will then respond with its
own public key. Currently no encryption is available, and this spec will change when
the beta is released to include encryption.

#### Message Transmission
The format for message transmission is JSON-encoded strings, specifically JSON objects
(more commonly known as maps or dictionaries).
The server requires a message field, which contains the user's messsage. The specifications
for standard communications also require the following:

| Key           | Data Type | Use                  |
|---------------|-----------|----------------------|
| `user`        | `string`  | Name of sender       |
| `message`     | `string`  | Message to display   |
| `color`       | `int`  | The user's preferred color. This should be a `curses` color code (0-7). |

Anything specified here *must* be sent by your client and can be expected to exist. You need
not concern yourself with checking for the existence of these fields because they are required
for the proper function of the client.

You may declare further data fields in your implementation, however you *must* check that they exist
because other clients likely will not implement them. These can be used to add useful functionality
such as nicknames, message formatting, and other message-specific signals.

## Footnotes
###### Links
[Link to this GitHub page.](https://github.com/SST-CTF/chatd)

[Link to our CTF (Programming) team / club.](http://sstctf.org)

###### Questions?
If you have any questions, feel free contact us: github@sstctf.org.
You can also contact the main author: stephen@sstctf.org.

###### Collaborators
Stephen Brimhall
