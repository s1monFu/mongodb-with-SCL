# mongodb-with-SCL
This program experiments with the possibility of replacing normal reader/writer locks in MongoDB with Scheduler-Operative locks (SCL). 
SCL is defined and developed in Patel et al's paper $Avoiding Scheduler Subversion using Schedulerâ€“Cooperative Locks$

The experiment runs on Oracle Cloud Infrastructure. The server is Ubuntu 20.04 and has 1 CPU and 1 GB of memory.
