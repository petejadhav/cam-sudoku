# Decentralized Secure Immutable P2P Chat

* No Central Server or master to host the chatroom
* Chat is stored on blockchain hosted on all clients
* PPK encryption used for 2 way communication


## Application Flow

* First client starts app.
    * public/private key generated
* Starts chatroom - 
    * New uuid generated & mapped to chatroom
    * New folder created - uuid, contains conf & peers file (some kind of DHT)
    * New blockchain initiated in uuid folder, genesis block contains chat-uuid and chatroom name
* Sends connect request to active peer
    * secure handshake - send public key and some data
    * peer sends back encrypted msg - sent data + some metadata
    * if data is verified - peer added to peers file - handshake successful
* Every new message sent encrypted using public key of recipient and added to blockchain
