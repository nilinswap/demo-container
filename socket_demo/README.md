# TCP vs UDP profiling

A client and server system is created and it is tested for speed against tcp and udp.

To test properly, I am using 2MB(250 pages) pdf. Client sending it in pieces of 500B, 1KB, 2KB

we are gonna run it in local system vs remote system


TCP

| | .5KB      | 1KB | 2KB |16KB|32KB|
|--------| ----------- | ----------- | -------- |--------|--------|
| local |     9ms    |   7ms     | 4ms  | 1.5ms| 2ms|
| remote | 1s|     1.2s  | 1.1s  |1.4s|



UDP

| | .5KB      | 1KB | 2KB |8KB|
|--------| ----------- | ----------- | -------- |--------|
| local |     14ms    |   9ms     | 5ms  | 2ms|
| remote | 17ms|     8ms  | 6ms  |2ms|

