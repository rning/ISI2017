# USC ISI 2017 Internship

## How to use this tool (Will currently only work on windows)
1. Run `TCP\TCPserver.py`
  - Make sure to input `'localhost'`, or the local IP of the server.
2. Run `TCP\TCPclient.py`
  - You must also input `'localhost'`, or the IP of the computer that is running `TCPserver.py`.
3. To view a graph of the data, run `TCP\timeVScwndPLOT.py`
4. *Optional* You can change some parameters for the simulation and then repeat steps 1-3. There is an explanation of the parameters below.

### Parameters
#### maxwnd: 
The maximum number of packets that can be sent at a time. This is the equivalent of a maximum advertised window or transfer limit on a network.

#### timeoutTime:
This is the amount of time that must be left for the server to wait to receive ACKs from the client.

#### programTotalMaxTime:
This is the total maximum time allotted for the program to run. It will automatically stop once this time is over.
(To cleanly close the programs in the case this does not occur, press ctrl + z.)

#### ssthreshEnabled:
This is whether or not to enable the server to send at a constant rate once it discovers the maximum window size.

#### Delay:
This is the delay on the simulation, and will slow it down or speed it up depending on size. A good default is 0.02.

## Goal Tracking
- [x] Scalable Send/Receive Between Client and Server nodes
- [x] Create trackable TCP simulation
  - [x] Slow Start
  - [x] Packet Loss
- [x] Create Visualization
  - [x] Remove tty prints
  - [x] Add log.txt printing
  - [x] Parse log.txt for x and y coord values

## Current Outputs

##### Current Thoughts on Errors
  *No Errors*
  
##### Possible Solutions
  *No Errors* 

#### TCPclient.py:
```
Output Message too long; Program working as intended anyway.
```

#### TCPserver.py:
```
Output Message too long; Program working as intended anyway.
```
