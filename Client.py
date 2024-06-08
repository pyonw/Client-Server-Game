# Sources https://docs.python.org/3.4/howto/sockets.html
# https://realpython.com/python-sockets/
# https://www.internalpointers.com/post/making-http-requests-sockets-python
# Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson
# youtube: https://www.youtube.com/watch?v=Ar94t2XhKzM
import socket

# Set server host and port
server_host = 'localhost'
server_port = 58974

# Create a socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_host, server_port))

print(f"Connected to: localhost on port: {server_port}")

done = False
prompt_message = "Enter '/q' to quit, '/game' to play Rock, Paper, Scissors, or a message to chat..... "
message_prompt = "Enter Input: "
invalid_choice_message = "Invalid choice! Please choose rock, paper, or scissors."
first_message_sent = False

while not done:
    # Display the initial prompt
    if not first_message_sent:
        print(prompt_message)
        first_message_sent = True
    else:
        user_input = input(message_prompt)
        client.send(user_input.encode('utf-8'))
        # Check if user wants to quit
        if user_input == '/q':
            done = True
            print("Shutting Down!")
        else:
            # Receive and display server response
            response = client.recv(1024).decode('utf-8')
            print("Server:", response)

client.close()