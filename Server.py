# Sources https://docs.python.org/3.4/howto/sockets.html
# https://realpython.com/python-sockets/
# https://www.internalpointers.com/post/making-http-requests-sockets-python
# Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson
# youtube: https://www.youtube.com/watch?v=Ar94t2XhKzM
import socket
import random

# Function to play Rock, Paper, Scissors
def play_game(client_choice):
    # define the choices for the game
    choices = ['rock', 'paper', 'scissors']
    # Generate a random choice for the server
    server_choice = random.choice(choices)

    # Determine the winner or if its tie
    if client_choice == server_choice:
        return "It's a tie! Server also chose " + server_choice
    elif (
        (client_choice == 'rock' and server_choice == 'scissors') or
        (client_choice == 'paper' and server_choice == 'rock') or
        (client_choice == 'scissors' and server_choice == 'paper')
    ):
        return "You win! Server chose " + server_choice
    else:
        return "You lose! Server chose " + server_choice

# Set up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 58974
server.bind(('localhost', port))
print(f"Server listening on: localhost on port: {port}")
server.listen()

# Accept client connection
client, addr = server.accept()
print(f"Connected by {addr}")
print("Waiting for message....")

done = False

while not done:
    # Receive message from the client
    msg = client.recv(1024).decode('utf-8')
    # Check the received message and take action based on the response
    if msg == '/q':
        done = True
        print("Client has requested shutdown... Shutting down!")
    elif msg == '/game':
        # Initiate game and handle game flow
        client.send("Enter your choice (rock, paper, scissors): ".encode('utf-8'))
        while True:
            user_choice = client.recv(1024).decode('utf-8')
            if user_choice.lower() in ['rock', 'paper', 'scissors']:
                # Play the game and send the result to the client
                result = play_game(user_choice.lower())
                client.send(result.encode('utf-8'))
                break
            else:
                # Send error message for invalid move
                client.send("Invalid choice! Please choose rock, paper, or scissors.".encode('utf-8'))
    else:
        print("Client:", msg)  # Displaying "Client:" before the user's message
        client.send(input("Message: ").encode('utf-8'))


# Close the client and server conections
client.close()
server.close()