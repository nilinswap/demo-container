# TCP vs UDP profiling

A client and server system is created and it is tested for speed against tcp and udp.

To test properly, I am using 2MB(250 pages) pdf. Client sending it in pieces of 500B, 1KB, 2KB

we are gonna run it in local system vs remote system


TCP

| | .5KB      | 1KB | 2KB |
|--------| ----------- | ----------- | -------- |
| local |       |   27ms     |   |
| remote |    |         |   |