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
'206.117.31.121'
handle_read reading...
received packet with seq# 1 ack# 0
sending ack
handle_read reading...
received packet with seq# 2 ack# 1
sending ack
handle_read reading...
received packet with seq# 3 ack# 2
sending ack
handle_read reading...
received packet with seq# 4 ack# 3
sending ack
handle_read reading...
received packet with seq# 5 ack# 4
***and it continues pretty much infinitely***
```

#### TCPserver.py:
```
Enter IP address of server in single quotes:
'206.117.31.121'
Server: Waiting for connection...
Server: Connection by  ('206.117.31.121', 49916)
readable:  False
writeable:  True
sent packet with seq# 1 ack# 0
readable:  True
handle_read reading...
acked 1 sequence 1 cwnd 1
readable:  False
writeable:  True
sent packet with seq# 2 ack# 1
readable:  True
handle_read reading...
acked 2 sequence 2 cwnd 1
readable:  False
writeable:  True
sent packet with seq# 3 ack# 2
readable:  True
handle_read reading...
acked 3 sequence 3 cwnd 1
readable:  False
writeable:  True
sent packet with seq# 4 ack# 3
readable:  True
handle_read reading...
acked 4 sequence 4 cwnd 1
readable:  False
writeable:  True
***and it continues pretty much infinitely***
```
