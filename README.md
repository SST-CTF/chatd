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


## Footnotes
###### Links
[Link to this GitHub page.](https://github.com/SST-CTF/chatd)

[Link to our CTF (Programming) team / club.](http://sstctf.org)

###### Questions?
If you have any questions, feel free contact us: github@sstctf.org.
You can also contact the main author: stephen@sstctf.org.

###### Collaborators
Stephen Brimhall
