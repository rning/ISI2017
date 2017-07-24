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
```

#### TCPserver.py:
```
Enter IP address of server in single quotes:
'10.1.1.2'
Server: Waiting for connection...
Server: Connection by  ('10.1.1.3', 32944)
sent packet with seq# 1 ack# 0
handle_read reading...
40
acked 1 sequence 1 cwnd 1
cwnd multiplied by 2, ssthresh:1
sent packet with seq# 2 ack# 1
sent packet with seq# 3 ack# 1
handle_read reading...
40
acked 2 sequence 2 cwnd 2
handle_read reading...
40
acked 3 sequence 3 cwnd 2
cwnd multiplied by 2, ssthresh:2
sent packet with seq# 4 ack# 3
sent packet with seq# 5 ack# 3
sent packet with seq# 6 ack# 3
sent packet with seq# 7 ack# 3
handle_read reading...
40
acked 4 sequence 4 cwnd 4
handle_read reading...
40
acked 5 sequence 5 cwnd 4
handle_read reading...
80
acked 6 sequence 6 cwnd 4
acked 7 sequence 7 cwnd 4
cwnd multiplied by 2, ssthresh:4
```
