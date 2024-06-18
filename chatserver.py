import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
      
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print(f"[DISCONNECTED] {client_address} disconnected.")
            break

        print(f"[{client_address}] {message}")

        
        client_socket.send(message.encode('utf-8'))

  
    client_socket.close()

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

def main():
    host = "127.0.0.1"  
    port = 12345 

    print("[STARTING] Server is starting...")
    start_server(host, port)

if __name__ == "__main__":
    main()


