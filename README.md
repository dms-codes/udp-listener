# UDP Data Receiver

This Python script is a UDP data receiver that listens for incoming UDP packets on a specified IP address and port. It processes the received data based on its length and extracts relevant information from different types of messages.

## Prerequisites

Before you begin, make sure you have the following:

- Python installed on your system.

## Usage

1. Clone this repository or download the script.

2. Open the script and make the following adjustments as needed:

   - Set the `UDP_IP` and `UDP_PORT` variables to specify the IP address and port on which you want to listen for UDP packets.

3. Run the script using the following command:

   ```bash
   python udp_data_receiver.py
   ```

4. The script will continuously listen for incoming UDP packets on the specified IP address and port.

5. It processes each received packet based on its length and extracts relevant information. There are three different message types supported:

   - Message length 35 bytes: Extracts software and software version information.
   - Message length 69 bytes: Extracts software, callee, caller, and report information.
   - Message length 106 bytes: Extracts software and message content.

6. The extracted information is printed to the console for each received packet.

## Example

Here's an example of what the script's output might look like:

```plaintext
35 Software: ABCD Version: 1234
69 Software: XYZW Callee: John Caller: Alice Report: OK
106 b'This is a sample message.\n'
```

## Note

- The script assumes that UDP packets it receives will adhere to specific message length patterns (35 bytes, 69 bytes, or 106 bytes). You may need to adapt the script if your UDP packets have different lengths or structures.

- Depending on your use case, you can customize the script to process the extracted information further, save it to a file, or perform any other desired actions.

Feel free to explore and customize the script to meet your specific requirements or integrate it into other projects as necessary.
