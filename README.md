# USC ISI 2017 Internship

## Goal Tracking
- [x] Scalable Send/Receive Between Client and Server nodes
- [ ] Create trackable TCP simulation
  - [ ] Slow Start
  - [ ] Packet Loss
- [ ] Create Visualization

## Current Outputs
#### TCPclient.py:
```
Enter IP address of server in single quotes:
'206.117.31.111'
handle_read reading...
received packet with seq# 1 ack# 0
sending ack
handle_read reading...
received packet with seq# 2 ack# 1
sending ack
handle_read reading...
received packet with seq# 3 ack# 1
sending ack
handle_read reading...
received packet with seq# 3 ack# 2
handle_read reading...
received packet with seq# 4 ack# 2
sending ack
handle_read reading...
received packet with seq# 5 ack# 2
sending ack
handle_read reading...
received packet with seq# 6 ack# 2
sending ack
handle_read reading...
Client: Connection Closed
error: uncaptured python exception, closing channel <__main__.Client 206.117.31.111:8080 at 0x28200c8> (<class 'struct.error'>:unpack requires a string argument of length 32 [C:\Python27\lib\asyncore.py|read|83] [C:\Python27\lib\asyncore.py|handle_read_event|449] [TCPclient.py|handle_read|23])
Client: Connection Closed
```

#### TCPserver.py:
```
Server: Connection by  ('206.117.31.111', 50687)
readable:  False
writeable:  True
sent packet with seq# 1 ack# 0
readable:  True
writeable:  False
handle_read reading...
acked 1 sequence 1 cwnd 1
acked 1 sequence 1 cwnd 1
acked 1 sequence 1 cwnd 1
acked 1 sequence 1 cwnd 1
ackedstartTime is NOT None
1entered timeout check
 1sequence  ==1  1cwnd
 multiplied cwnd by 21

readable:  False
writeable:  True
sent packet with seq# 2 ack# 1
sent packet with seq# 3 ack# 1
readable:  True
writeable:  False
handle_read reading...
ackedstartTime is NOT None
2entered timeout check
sequence2  2==  cwnd2
2multiplied cwnd by 2

readable:  False
writeable:  True
sent packet with seq# 3 ack# 2
sent packet with seq#startTime is NOT None
4entered timeout check
ack#2  2==
 sent packet with seq#2
5multiplied cwnd by 2
ack# 2
sent packet with seq# 6 ack# startTime is NOT None2

readable: entered timeout check
True2
 writeable: ==  False2

handle_read reading...multiplied cwnd by 2

error: uncaptured python exception, closing channel <__main__.EchoServer connected 206.117.31.111:50687 at 0x39c1e88> (<class 'struct.error'>:unpack requires a string argument of length 32 [C:\Python27\lib\asyncore.py|read|83] [C:\Python27\lib\asyncore.py|handle_read_event|449] [TCPserver.py|handle_read|59])
```
