Rock, Paper, Scissors Chat Server

**Overview**

This project implements a basic client-server architecture using sockets in Python. It allows a client to connect to a server to either chat or play a game of Rock, Paper, Scissors. The server handles multiple client requests such as initiating a game, chatting, and terminating the connection.

**Features**

Chat Functionality: Send and receive messages between the client and server.
Game Mode: Play Rock, Paper, Scissors with the server.
Connection Management: Handles client connections, receives client inputs, and sends appropriate responses.
How to Run

**Server**
Navigate to the directory containing Server.py.
Run the script using Python:
python Server.py
The server will start and listen for connections on localhost on a predefined port.

**Client**
Navigate to the directory containing Client.py.
Run the script using Python:
python Client.py
The client will automatically try to connect to the server. Follow the on-screen prompts to send messages or start a game.
Commands

/q: Disconnect from the server.
/game: Start a game of Rock, Paper, Scissors. You will be prompted to enter your choice (rock, paper, or scissors).

**Dependencies**

Python 3.4 or higher
socket library (included in standard Python library)

**Sources and Acknowledgments**

Python socket programming guide: Python Docs
Real Python sockets tutorial: Real Python
Internal Pointers on making HTTP requests with sockets: Internal Pointers
Kurose and Ross, "Computer Networking: A Top-Down Approach", 8th Edition, Pearson
YouTube tutorial: Python Sockets
Feel free to adjust the content or add more details if needed! ​​
