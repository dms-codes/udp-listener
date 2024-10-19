import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 2237
BUFFER_SIZE = 1024

# Initialize and bind the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def handle_35_byte_message(data):
    """Process and print a message with 35 bytes of data."""
    software = data[16:20].decode()
    sw_version = data[28:].decode()
    result = f'Software: {software} Version: {sw_version}'
    print("35-byte message:", result)

def handle_69_byte_message(data):
    """Process and print a message with 69 bytes of data."""
    software = data[16:20].decode()
    callee, caller, report = data[50:].decode().split(" ")
    print("69-byte message:", software, callee, caller, report)

def handle_106_byte_message(data):
    """Process and print a message with 106 bytes of data."""
    software = data[16:21].decode()
    message = data[29:64].decode()
    print(f"106-byte message - Software: {software}\nMessage: {message}\n")

def process_data(data):
    """Route the received data to the appropriate handler based on length."""
    data_len = len(data)
    
    if data_len == 35:
        handle_35_byte_message(data)
    elif data_len == 69:
        handle_69_byte_message(data)
    elif data_len == 106:
        handle_106_byte_message(data)
    else:
        print(f"Unhandled message length: {data_len}")

# Main loop to receive and process data
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    process_data(data)
