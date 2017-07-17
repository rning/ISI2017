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
handle_read reading...
received packet with seq# 1 ack# 0
sending ack
handle_read reading...
```

#### TCPserver.py:
```
Server: Connection by  ('206.117.31.121', 52170)
sent packet with seq# 1 ack# 0
packetController called
handle_read reading...
acked 1 sequence 1 cwnd 1
handle_write sending...
packetController called
handle_write sending...
packetController called
...
```
