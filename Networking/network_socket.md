<div align="center">
  <h1> Network Sockets </h1>
</div>

A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. The structure and properties of a socket are defined by an application programming interface (API) for the networking architecture. Sockets are created only during the lifetime of a process of an application running in the node. <br>

Because of the standardization of the TCP/IP protocols in the development of the internet, the term *network socket* is most commonly used in the context of the internet protocol suite, and is therefore often also referred to as the **internet socket**. In this context, a socket is externally identified to other hosts by it's **socket address**, which is the triad of transport protocol, IP address and port number. <br>

The term *socket* is also used for the software endpoint of node-internal inter-process communication (IPC), which often uses the same API as a network socket.

## Use

The application programming interface (API) for the network protocol stack creates a handle for each socket created by an application, commonly referred to as a *socket descriptor*. In Unix-like operating systems, this descriptor is a type of file descriptor. It is stored by the application process for use with every read and write operation on the communication channel. <br>

At the time of creation with the API, a network socket is bound to the combination of a type of network protocol to be used for transmissions, a network address of the host and a port number. Ports are numbered resources that represent another type of software structure of the node. They are used as service types and once created by a process, serve as an externally (from the network) addressable location component, so that other hosts may establish connections. <br>

Network sockets may be dedicated for persistent connections for communication between two nodes (e.g. TCP), or they may participate in connection and multicast communcations (e.g. UDP) <br>

In practice, due to the proliferation of the TCP/IP protocols in use on the internet, the term *network socket* usually refers to the use with the Internet Protocol (IP). It is therefore also called **internet socket**.

## Socket Addresses

An application can communicate with a remote process by exchanging data with TCP/IP by knowing the combination of protocol type, IP address and port number. This combination is often known as a *socket address*. It is the network-facing access handle to the network socket. The remote process establishes a network socket in its own instance of the protocol stack, and uses the networking API to connect to the application, presenting its own socket address for use by the application.

## Implementation

A protocol stack, usually provided by the operating system (rather than a seperate library, for instance), is a set of services that allow processes to communicate over a network using the protocols that the stack implements. The operating system forwards the payload of incoming IP packets to the corresponding application by extracting the socket address information from the IP and transport protocol headers and stripping the headers from the application data. <br>

The API that programs use to communicate with the protocol stack, using network sockets, is called a **socket API**. Development of application programs that utilize this API is called socket programming or network programming. Internet socket API's are usually based on the Berkeley socket standard. In the Berekeley sockets standard, sockets are a form of file descriptor, due to the Unix philosophy that "everything is a file", and the analogies between sockets and files. Both have functions to read, write, open and close. In practice the differences strain the analogy, and different interfaces (send and receive) are used on a socket. In inter-process communication each end generally has its own socket. <br>

In the standard Internet protocols TCP and UDP, a socket address is the combination of an IP address and a port number, much like one end of a telephone connection is the combination of a phone number and a particular extension. Sockets need not have a source address, for example, for only sending data, but if a program binds a socket to a source address, the socket can be used to receive data sent to that address. Based on this address, Internet sockets deliver incoming data packets to the appropiate application process. <br>

**Socket** often refers specifically to an internet socket or TCP socket. An internet socket is minimally characterized by the following;

1. `local socket address:` Consisting of the local IP address and (for TCP and UDP, but no IP) a port number.
2. `protocol:` A transport protocol, e.g. TCP, UDP, raw IP. This means that (local or remote) endpoints with TCP port 53 and UDP port 53 are distinct sockets, while IOP does not have ports.
3. A socket that has been connected to another socket, e.g. during the establishment of a TCP connection, also has a remote socket address.


## Types

### Datagram sockets

**Connectionless sockets, which use User Datagram Protocol (UDP)**. Each packet sent or received on a datagram socket is individually addressed and routed. Order and reliability are not guaranteed with datagram sockets, so multiple packets sent from one machine or process to another may arrive in any order or might no arrive at all. Special configuration may be required to send broadcasts on a datagram socket. In order to receive broadcast packets, a datagram socket should not be bound to a specific address, though in some implementations, broadcast packets may also be received when a datagram socket is bound to a specific address.

### Stream sockets

**Connection-oriented sockets, which use Transmission Control Protocol (TCP)**, Stream Controls Transmission Protocol (SCTP) or Datagram Congestion Control Protocol (DCCP). A stream socket provides a sequenced and unique flow of error-free data without record boundaries, with well-defined mechanisms for creating and destroying connections and reporting errors. A stream socket transmits data reliably, in order and without out-of-bound capabilities. On the internet, stream sockets are typically implemented using TCP so that applications can run across any networks using TCP/IP protocol.

### Raw sockets

Allow direct sending and receiving of IP packets without any protocol-specific transport layer formatting. With other types of sockets, the payload is automatically encapsulated according to the chosen transport layer protocol (e.g. TCP, UDP), and the socket user is unaware of the existence of protocol headers that are broadcast with the payload. When reading from a raw socket, the headers are usually included. When transmitting packets from a raw socket, the automatic addition of a header is optional.

## Socket states in the client-server model

Computer processes that provide application services are referred to as servers and create sockets on startup that in the *listening state*.These sockets are waiting for initiatives from client programs. <br>

A TCP server may serve several clients concurrently by creating a unique dedicated socket for each client connection in a new child process or processing thread for each client. These are in the established state when a socket-to-socket virtual connection or virtual circuit (VC), also known as a TCP session, is established with the remote socket, providing a duplex byte stream. <br>

A server may create several concurrently established TCP sockets with the same local port number and local IP address, each mapped to its own server-child process, serving its own client process. They are treated as different sockets by the operating system since the remote socket address (the client IP address or port number) is different; i.e. since they have different socket pair tuples. <br>

UDP sockets do not have an established connection state, because the protocol is connectionless. A UDP server process handles incoming datagrams from all remote clients sequentially through the same socket. UDP sosckets are not identified by the remote address, but only by the local address, although each message has an associated remote address that can be retrieved from each datagram with the networking API.

## Socket pairs

Communicating local and remote sockets are **socket pairs**. Each socket pair is described by a unique 4-tuple consisting of source and destination IP addresses and port numbers of the local and remote socket addresses, i.e. `(Local IP address, Local port number, Remote IP address, Remote port number)`. As discussed above, in the TCP case, a socket pair is associated on each end of the connection with a unique 4-tuple.