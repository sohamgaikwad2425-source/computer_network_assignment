Question 1: Client-Server Socket Programming
Aim

To write a Python program using socket programming to implement a simple client-server network architecture where a client sends a text message to a server.

Theory

Socket programming allows two applications to communicate over a network. In a client-server architecture, the server waits for a connection while the client initiates the connection.

In this experiment, TCP socket programming is used. The server listens on 127.0.0.1 at port 5000. The client connects to the server and sends a text message. The server receives the message and sends a confirmation response back to the client.

Files Used
Question_1/server.py
Question_1/client.py
Procedure
Create a TCP socket on the server.
Bind the server socket to IP address 127.0.0.1 and port 5000.
Start listening for client connections.
Create a client socket and connect it to the server.
Enter a text message on the client.
Send the message to the server.
The server receives and displays the message.
The server sends a response to the client.
Close the connection.
Sample Output

Client:

Enter message to send to server: Hello Server
Server response: Message received successfully by the server.

Server:

Server is waiting for connection...
Connected to: ('127.0.0.1', ...)
Message from client: Hello Server
Result

The client successfully connected to the server and exchanged a text message using TCP socket programming.

Question 2: Network Device Classification
Aim

To write a Python script that classifies network devices and transmission media according to their layer of operation and primary function.

Theory

Network devices perform different functions in a network topology.

Device Layer Primary Function
Switch Data Link Layer (Layer 2) Connects devices in a LAN and forwards frames using MAC addresses.
Router Network Layer (Layer 3) Connects different networks and forwards packets using IP addresses.
Bridge Data Link Layer (Layer 2) Connects and filters traffic between LAN segments.
Access Point Data Link Layer (Layer 2) Provides wireless access and connects wireless devices to a LAN.
Transmission Media
Media Description
Ethernet Cable Wired medium commonly used for LAN communication.
Fiber Optic Cable High-speed wired medium that transmits data using light.
Wireless Uses radio waves for communication without physical cables.
Files Used
Question_2/network_classification.py
Sample Output
NETWORK DEVICE CLASSIFICATION REPORT

Device: Switch
Layer: Data Link Layer (Layer 2)
Primary Function: Connects devices in a LAN and forwards frames using MAC addresses.

Device: Router
Layer: Network Layer (Layer 3)
Primary Function: Connects different networks and forwards packets using IP addresses.

Device: Bridge
Layer: Data Link Layer (Layer 2)
Primary Function: Connects and filters traffic between LAN segments.

Device: Access Point
Layer: Data Link Layer (Layer 2)
Primary Function: Provides wireless access and connects wireless devices to a LAN.
Result

The Python program successfully classified the given network devices according to their OSI layer and primary function. It also described the different transmission media used in networking.

Conclusion

The experiment successfully demonstrated basic networking concepts using Python. The first question implemented client-server communication using TCP sockets, while the second question classified common network devices and transmission media based on their functions and network layers.
