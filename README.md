SST CTF chatd
=============

This is a chat service for the SST CTF server. When complete, it will use RSA keypairs
for data encryption and SCP/SFTP for file transfer, making it quite secure. Users will
log in using their server logon name and the server will verify their identity through
`~/.ssh/authorized_keys`. If they are authorized, the server will allow them to
connect. The client will transmit his/her public key on login to enable secure
communications. This server will respond with its public key to facilitate this secure
communication. This key will be encrypted with the client's public key to help foil
man-in-the-middle attacks.