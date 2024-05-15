import socket

host = "localhost"  
port = 9999

def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print("Connected to the server.")

            while True:
                response = client_socket.recv(1024).decode()
                print(response)

                if "Choose a difficulty level" in response:
                    difficulty = input("Enter the difficulty level (low/moderate/hard): ")
                    client_socket.sendall(difficulty.encode())
                elif "Enter your guess" in response:
                    guess = input("Enter your guess: ")
                    client_socket.sendall(guess.encode())
                elif "Correct Answer!" in response:
                    name = input("Enter your name: ")
                    client_socket.sendall(name.encode())
                    leaderboard = client_socket.recv(4096).decode()
                    print("\nLeaderboard:")
                    print(leaderboard)
                    break

            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.lower() != 'y':
                break

if __name__ == "__main__":
    main()
