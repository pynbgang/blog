---
layout: post
title: "tcp topic list"
published: true
created:  2020 Jan 28 11:02:29 AM
tags: [tcp]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# TCP topics

* format
* how seq is generated? (time based? randomly? from 1?)
  - Owen:The operating system is free to use any mechanism it likes, but generally it's best if it chooses a random number, as this is more secur
* how seq:ack works: ack# is the "expected next seq#"
* state machine (TODO)
* delayed ack (200ms): to wait and accumulate more data to be sent along with the ack.
* Nagle algorithm: allow one outstanding nont-acked small segment only. send more only after its ack received
* advertised win(sliding window): by receiver
* (sliding) windows update (via a special ack)
* PUSH: indicate to receiver, don't wait for more data, just give to high level app.
* TCP MSS: IP MTU1500-IP20-TCP20=1460
    - the largest amount of bytes can be received in a single TCP segment. 
    - not count the IP or TCP header
    - can be diff in each direction (not "negotiated" really)
* TCP "urgent mode", with urgent bit of TCP flags and 16b of "urgent pointer": telnet (not quite get it)

* TCP timeout and retransmission
  - exponential backoff
  - from 1st pkt to rst, ~ 9min, changable in some xnix via tcp_ip_abort_interval
  - RTT: from send a pkt to get its ack
  - RTT measure
  - RTO: how long time to wait before we assume the pkt was lost and needs retransmission? based on RTT measure
  - https://blog.csdn.net/wdscq1234/article/details/52505191
  - karn algorithm (not quite get it)

* slow start
    - the way to initiate data flow
    - congestion window(cwnd): used by sender. start from 1, double when get ack. 
    - current (overall) windows size of a session = min(cwnd, advertised win)
    - sender will send based on current windows size

* congestion avoidance:
  - after congestion happens
  - algorithm independent of slow start, but implemented together when congestion happens
  - dup ack: 
    *** to indicate ooo (out of order)
    *** sender sent 1,2,3,4; recver get 1,2,4; recver will send 2 ack of 2, to indicate miss of 3.
  - congestion indicators: timeout or received dup of Ack
  - ssthresh counter: set max(current_win/2, 2)
  - increase cwnd by 1/cwnd each time an ACK is received

* how congestion avoidance works with slow start:
  - when a session init: cwnd, ssthresh=1, 655535
  - sender: send min(cwnd, recver_advertised_win) pkts
  - on congestion (dup ack, timeout): 
    *** ssthresh=max(current_win/2, 2)
    *** if timeout: also do slow start
        **** set cwnd=1
        **** on each ACK receive: cwnd*=2
        **** until cwnd >= ssthresh
        **** then change to congestion avoidance: cwnd+=1
  - ![visualization](https://user-images.githubusercontent.com/2038044/73123679-4e392680-3f60-11ea-8a14-52e48e6368f5.png)

* fast retransmit and fast recovery:
  - on >=3 dup ack: retransmit w/ waiting for timeout     => fast retransmit
  - then start congestion avoidence instead of slow start => fast recovery

* persist timer (60s)
  - receiver: send win0 ack
  - sender: send win probe every persist timer, 
  - why? because ack is not reliable, if ack get lost session will get stuck
  - avoid "silly window": not to update small win or send small segment

* TCP keepalive timer:
  - on good connection: 2 hours after last moment of data transmission
  - when client no reponding: send a KA every 75s and reset after 10*75s
  - when client restarted: get a RST, and reset connection
  - KA probe is an ack w/o data, with a wrong seq# (seq = next seq - 1), 
  - this triggers an ack from peer, with ack# being next seq#
  - ARP is triggered before KA sent, KA is sent only when ARP get replied
  - in same LAN, when client gone no ARP reply will be received. so all 10*75s will be arp instead of TCP.
  - in WAN, if client is not reachable, router will give ICMP net unreachable on each tcp KA*75s

* TCP new feature/options:
  - selective acknowledge
  - window scale option
  - timestamp (protection against wrapped sequence numbers - PAWS)
  - improved transactional processing using TCP
  - path MTU discovery (obsolete?)

* global synchronization
