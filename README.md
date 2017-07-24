# USC ISI 2017 Internship

## Goal Tracking
- [x] Scalable Send/Receive Between Client and Server nodes
- [ ] Create trackable TCP simulation
  - [ ] Slow Start
  - [ ] Packet Loss
- [ ] Create Visualization

## Current Outputs

##### Current Thoughts on Errors
  *No Errors*
  
##### Possible Solutions
  *No Errors* 

#### TCPclient.py:
```
Enter IP address of server in single quotes:
'10.1.1.2'
handle_read reading...
40
received packet with seq# 1 ack# 0
sending ack
handle_read reading...
40
received packet with seq# 2 ack# 1
sending ack
handle_read reading...
40
received packet with seq# 3 ack# 1
sending ack
handle_read reading...
40
received packet with seq# 4 ack# 3
sending ack
handle_read reading...
120
received packet with seq# 5 ack# 3
sending ack
received packet with seq# 6 ack# 3
sending ack
received packet with seq# 7 ack# 3
sending ack
handle_read reading...
40
received packet with seq# 8 ack# 7
sending ack
handle_read reading...
280
received packet with seq# 9 ack# 7
sending ack
received packet with seq# 10 ack# 7
sending ack
received packet with seq# 11 ack# 7
sending ack
received packet with seq# 12 ack# 7
sending ack
received packet with seq# 13 ack# 7
sending ack
received packet with seq# 14 ack# 7
sending ack
received packet with seq# 15 ack# 7
sending ack
handle_read reading...
40
received packet with seq# 16 ack# 15
sending ack
handle_read reading...
600
received packet with seq# 17 ack# 15
sending ack
received packet with seq# 18 ack# 15
sending ack
received packet with seq# 19 ack# 15
sending ack
received packet with seq# 20 ack# 15
sending ack
received packet with seq# 21 ack# 15
sending ack
received packet with seq# 22 ack# 15
sending ack
received packet with seq# 23 ack# 15
sending ack
received packet with seq# 24 ack# 15
sending ack
received packet with seq# 25 ack# 15
sending ack
received packet with seq# 26 ack# 15
sending ack
received packet with seq# 27 ack# 15
sending ack
received packet with seq# 28 ack# 15
sending ack
received packet with seq# 29 ack# 15
sending ack
received packet with seq# 30 ack# 15
sending ack
received packet with seq# 31 ack# 15
sending ack
handle_read reading...
40
received packet with seq# 16 ack# 15
redefined ack, sending ack
handle_read reading...
280
received packet with seq# 17 ack# 15
sending ack
received packet with seq# 18 ack# 15
sending ack
received packet with seq# 19 ack# 15
sending ack
received packet with seq# 20 ack# 15
sending ack
received packet with seq# 21 ack# 15
sending ack
received packet with seq# 22 ack# 15
sending ack
received packet with seq# 23 ack# 15
sending ack
handle_read reading...
```

#### TCPserver.py:
```
Enter IP address of server in single quotes:
'10.1.1.2'
Server: Waiting for connection...
Server: Connection by  ('10.1.1.3', 33028)
sent packet with seq# 1 ack# 0
handle_read reading...
acked 1 sequence 1 cwnd 1
cwnd multiplied by 2, ssthresh:1
sent packet with seq# 2 ack# 1
sent packet with seq# 3 ack# 1
handle_read reading...
acked 2 sequence 2 cwnd 2
handle_read reading...
acked 3 sequence 3 cwnd 2
cwnd multiplied by 2, ssthresh:2
sent packet with seq# 4 ack# 3
sent packet with seq# 5 ack# 3
sent packet with seq# 6 ack# 3
sent packet with seq# 7 ack# 3
handle_read reading...
acked 4 sequence 4 cwnd 4
handle_read reading...
acked 5 sequence 5 cwnd 4
handle_read reading...
acked 6 sequence 6 cwnd 4
acked 7 sequence 7 cwnd 4
cwnd multiplied by 2, ssthresh:4
sent packet with seq# 8 ack# 7
sent packet with seq# 9 ack# 7
sent packet with seq# 10 ack# 7
sent packet with seq# 11 ack# 7
sent packet with seq# 12 ack# 7
sent packet with seq# 13 ack# 7
sent packet with seq# 14 ack# 7
sent packet with seq# 15 ack# 7
handle_read reading...
acked 8 sequence 8 cwnd 8
handle_read reading...
acked 9 sequence 9 cwnd 8
handle_read reading...
acked 10 sequence 10 cwnd 8
acked 11 sequence 11 cwnd 8
acked 12 sequence 12 cwnd 8
acked 13 sequence 13 cwnd 8
acked 14 sequence 14 cwnd 8
acked 15 sequence 15 cwnd 8
cwnd multiplied by 2, ssthresh:8
sent packet with seq# 16 ack# 15
sent packet with seq# 17 ack# 15
sent packet with seq# 18 ack# 15
sent packet with seq# 19 ack# 15
sent packet with seq# 20 ack# 15
sent packet with seq# 21 ack# 15
sent packet with seq# 22 ack# 15
sent packet with seq# 23 ack# 15
sent packet with seq# 24 ack# 15
sent packet with seq# 25 ack# 15
sent packet with seq# 26 ack# 15
sent packet with seq# 27 ack# 15
sent packet with seq# 28 ack# 15
sent packet with seq# 29 ack# 15
sent packet with seq# 30 ack# 15
sent packet with seq# 31 ack# 15
handle_read reading...
acked 16 sequence 16 cwnd 16
handle_read reading...
acked 17 sequence 17 cwnd 16
exceeded wnd, -> retransmit
sent packet with seq# 16 ack# 15
sent packet with seq# 17 ack# 15
sent packet with seq# 18 ack# 15
sent packet with seq# 19 ack# 15
sent packet with seq# 20 ack# 15
sent packet with seq# 21 ack# 15
sent packet with seq# 22 ack# 15
sent packet with seq# 23 ack# 15
handle_read reading...
handle_read reading...
acked 16 sequence 16 cwnd 8
handle_read reading...
acked 17 sequence 17 cwnd 8
acked 18 sequence 18 cwnd 8
acked 19 sequence 19 cwnd 8
acked 20 sequence 20 cwnd 8
acked 21 sequence 21 cwnd 8
acked 22 sequence 22 cwnd 8
exceeded wnd, -> retransmit
acked 7 sequence 7 cwnd 4
sent packet with seq# 8 ack# 7
sent packet with seq# 9 ack# 7
sent packet with seq# 10 ack# 7
sent packet with seq# 11 ack# 7
handle_read reading...
acked 8 sequence 8 cwnd 4
handle_read reading...
acked 9 sequence 9 cwnd 4
handle_read reading...
acked 10 sequence 10 cwnd 4
acked 11 sequence 11 cwnd 4
timeout -> retransmit
sent packet with seq# 12 ack# 11
sent packet with seq# 13 ack# 11
```
