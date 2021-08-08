# [ultimate-hands-on-hadoop](https://github.com/murshidazher/ultimate-hands-on-hadoop)

> Hadoop with HDFS, YARN, MapReduce, Pig, Hive, Spark, Flink and more...

- This repository contains all the data, setup and execution scripts used during the coursework on [Udemy - The Ultimate Hands on hadoop Tame your Big data](https://www.udemy.com/the-ultimate-hands-on-hadoop-tame-your-big-data/)
- Requires Hortonworks Sandbox 2.6.5, for docker script to run locally look into this [repo](https://github.com/murshidazher/hdp-docker-sandbox).
- If you need terraform script to setup an sandbox environment in AWS, look into this [repo](https://github.com/murshidazher/terraform-hdp).

## Table of Contents

- [ultimate-hands-on-hadoop](#ultimate-hands-on-hadoop)
  - [Table of Contents](#table-of-contents)
  - [Quick Navigation by Technology](#quick-navigation-by-technology)
  - [Notes](#notes)
    - [Data Ingestion](#data-ingestion)
    - [External data storage](#external-data-storage)
    - [Query Engines](#query-engines)
  - [Tech Stack](#tech-stack)
    - [Core](#core)
    - [Querying](#querying)
    - [Ingestion](#ingestion)
    - [NoSQL Databases](#nosql-databases)
    - [Streaming](#streaming)
    - [Notebooks and Visualization](#notebooks-and-visualization)
    - [Other](#other)
  - [License](#license)

## Quick Navigation by Technology

- [ml-100k](./section-01)
- [MR using Python](./section-02)
- [PigLatin and Pig](./section-03)
- [Spark](./section-04)
- [Hive](./section-05)
- [HBase, MongoDB & Cassandra](./section-06)
- [Drill, Phoenix, Presto](./section-07)
- [Yarn, Tez, Mesos, Zookeeper, Oozie, Hue](./section-08)
- [Real time Ingestion - kafka and flume](./section-09)
- [Spark Streaming, Apache Storm & Apache Flink](./section-10)
- [Apache Flume](./section-11)

## Notes

`HDFS` → `MapReduce` (distributed processing is made possible by MapReduce) → `Pig` →  `Hive`

`MRv1` mapreduce legacy architecture vs new architecture with `YARN`

Sitting on top of hdfs is `YARN` (yet another resource negotiator) - data processing comes in this place. Its what decides what gets run tasks when and what nodes are available for the work it is like a heartbeat to see which nodes are available and not. MapReduce allows you do parallel computing and process the data in parallel across the cluster. Originally, Yarn and mapreduce were the same but later split on so that other application can be built on top of YARN.

Sitting on top of  `MapReduce` is `pig`, if we dont want to write java or python map reduce code, we can use SQL style scripting language which is PIG. We can chain together queries and get the processing.Hive sits on top of mapreduce too and it solves the same problem as PIG its really more directly works like a SQL database. It makes all the files that is sitting on the file system like a SQL database. So we can make SQL queries on it.  But underneath its not really a SQL database.

`Apache Ambari` sits on top of all these and it gives a general overview of all by sitting on top of the cluster. How much resources are used, import database, run hive queries. Ambari is what hortonworks uses , there are others too like cloudera, MapR.

`MESOS` is not part of hadoop but its an alternative for YARN. So its too is a resource negotiator to manage the resources in the cluster.

`Spark` is same level as mapreduce and it sits on top of `YARN` or `MESOS`. It actually runs queries on the data. We need to write program in either python, java or scala (preferred). Extremely fast and exciting technology if we need to process data fast and reliably in the hadoop cluster then its the resource. It can handle streaming data, machine learning, etc...

`Tez` is similar to spark and uses similar technologies like directed acyclic graph. Tez is used in conjunction with hive to accelerate the process and queries. Hive through tez is faster than hive with mapreduce.

`Apache HBase` is a way to exposing the data in your cluster to transactional platform. Hbase is what we call a nosql database, its a columnar datastore. `HBase` lets us expose the data stored in the cluster and provides a fast way to exposing that data.

`Apache Storm` is a way of processing stream data in real-time. So if we have streaming data from sensors or other ways then we can process it in real time. Spark streaming solves the same problem and its an alternative while storms solves it in another way.  It doesnt have to be a batch processing anymore and we can update the machine learning model as it comes in.

`Oozie` is just a way of scheduling jobs on your clusters. So if we have a task that need to happen in the cluster and involves many different systems then oozie is the way of scheduling it into a job and run of some sort of schedule. ex. loading the data into hive, and querying it using pig and work with spark and then transforming the result using hbase. oozie can manage this all for you and manage it reliably.

`Zookeeper` is used to coordinate everything inside the cluster. So its the technology which knows which nodes are up and which nodes are down and share the system state reliably across the cluster even when a node randomly goes down. Who is the master and slave.

### Data Ingestion

> how do you get data into the cluster into HDFS from external sources

`Sqoop` - a way of tieing the hadoop database into a relational database. Anything which can talk to ODBC or JDBC can be transformed into scoop into a hdfs file system. scoop is a connector from hdfs to legacy databases.

`Flume` - is a way of transporting web logs in large scale and very reliably to the cluster. If we have a fleet of web servers, flume can listen to their web logs coming in from those web services in real time and publish them into your cluster in real time for processing by something like strom or Spark streaming.

`Kafka` - solves a similar problem but is a little bit more general purpose. It can basically collect data from any sort from a cluster of PCs from a cluster of web servers or whatever its and broadcast it to hadoop.

### External data storage

We can import and export data using the scoop to mysql.

`Cassandra` or `mongodb` like `hbase` is used to expose the data to external api.

### Query Engines

There are several query engines which also sits on top of the hadoop cluster. So if we want to interactively enter sql queries. hive is also similar thing but since hive is tightly integrated with hadoop we dont consider it.

`Apache drill` - allows you to write SQL queries that will work across a wide range of NoSQL databases. It can actually talk to the hbase database and maybe cassandra or mongodb. Tie those results altogether and allow you to write queries across all those disparate data stores and bring them all back together when you're done.

`Hue` - actually for cloudera which takes the role of ambari as sort of things that lets you visualize and execute queries on the Hadoop cluster as a whole.

`Apache Phoenix` - kind of similar to drill it lets you do SQL style queries across the entire range of data storage technologies you might have but it takes it one step further and it actually gives you ACID guarantees and OLTP. So you can actually make your not Sql hadoop datastore look like a relational database.

`Presto`  - yet another way to write queries

`Apache zepplin` - just takes an another angle on it that takes more of a notebook type approach to the ui and how you actually interact with the cluster.

## Tech Stack

> All the technologies uses throughout the course

### Core

- [x] Introduction to the Hadoop Eco-system
- [x] YARN
- [x] HDFS
- [x] MapReduce
- [x] Pig
- [x] Spark
- [x] Hive
- [x] Tez
- [x] Mesos - Alternative cluster manager for `YARN`
- [x] Zookeeper
- [x] Oozie

### Querying

- [x] Apache Drill
- [x] Apache Phoenix
- [x] Presto

### Ingestion

- [x] Sqoop
- [x] Kafka
- [x] Flume

### NoSQL Databases

- [x] HBase
- [x] Cassandra
- [x] MongoDB

### Streaming

- [x] Spark Streaming
- [ ] Storm
- [ ] Flink

### Notebooks and Visualization

- [ ] Apache Zeppelin
- [ ] Apache Superset

### Other

- [ ] Impala
- [ ] Accumulo
- [ ] Redis
- [ ] Ignite
- [ ] Elasticsearch
- [ ] Kinesis
- [ ] Apache NiFi
- [ ] Falcon
- [ ] Apache Slider

## License

[MIT](./LICENSE) © Murshid Azher.
