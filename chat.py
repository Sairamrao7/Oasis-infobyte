import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except Exception as e:
        print(f"Connection error: {e}")
        return

    print(f"[CONNECTED] Connected to {host}:{port}")

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))

    client.close()

def main():
    host = "127.0.0.1"  
    port = 12345 
    print("[STARTING] Client is starting...")
    start_client(host, port)

if __name__ == "__main__":
    main()
