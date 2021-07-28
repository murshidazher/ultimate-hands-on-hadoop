# NoSQL

Doing analytics in RDBMS is great but if we need to really quickly search on millions of dataset like what google has then we need to use NoSQL since RDBMS will not cut it out. Like what the user searched previously, what they buy previously and etc...

- HBase - built on top of HDFS.
- Cassandra
- MongoDB

## Before NoSQL

Before NoSQL in Amazon to scale up a MySQL database we needed to take extreme measures,

- Denormalization (Split up your tables into a lot of tables to query a particular set of data, and it can look very ugly)

- Caching Layers (Using memCachedD distributed in memory to prevent queries from even reaching the database for a lot of traffic, but cache could run into issues like not being synchronized with database)

- Master/Slave setups (Multiple databases that handles reads and writes and the rest gets replicated to handles reads or writes but it requires a Database administrator)

- Sharding (Split database into different ranges where it handles a range of keys, but setting it and adding new shards is a very painful process)

- Materialized Views (Show views in the format that your services expects)

- Removing stored procedures (Removing computing stuff that is actually part of a process of processing a query is an expensive thing to do, so you have to give that up)

## RDBMS will in fact have support nightmares for that planet size queries and transactions rates

## HBase

- Its an opensource implementation of Google's BigTable paper
- Each cell in a column family can have different timestamp. We can stay that retain all the updates for the last three days.
- `com.cnn.www` is how google saves it because you can instantly reduce the number of records filtered with the `com` rather than `www`.

![How google saves page visits in google bigtable](./docs/01.png)

## Creating an HBase table and Querying it with Python

> The script is available here [HBaseExamples.py](./HBaseExamples.py).

- Implementation details available in [ImportMovieRatingsIntoHBase](./Section6-42 ImportMovieRatingsIntoHBase.txt).
- `Rating` is the column family name and `50` is the actual column name.
- We will create a python script that given the information constructs a hbase table similar to the image.
- The python would be running in the local machine white the hbase would be running inside the sandbox instance. 
- We need to open port `8000` for rest api.
- In the sandbox, make sure that the Hbase service is started.

![example hbase table impl](./docs/02.png)

![impl python architecture](./docs/03.png)

We will use the `starbase` which is a hbase wrapper written in python,

```sh
> pip install starbase
```

## Hbase with Pig Integration

> The hbase with pig file is available at [hbase.pig](./hbase.pig)

- Populate an HBase table with big data, source from the local hdfs and then to put into the hbase.
- We need to make sure that the table name is already created in hbase and we have a unique key value as the row identifier.
- Implementation details available in [UseHBaseWithPigToImportData](./Section6-43 UseHBaseWithPigToImportData.txt).
- upload the `u.user` from `ml-100k` to see the relations between them.

```sh
> hbase shell # to get into the interactive shell
hbase> list
hbase> create 'users', 'userinfo'
hbase> exit
> pig hbase.pig
```

When dropping a table in hbase we need to disable it first,

```sh
hbase> disable 'users'
hbase> drop 'users'
```

HBase is not always the best choice when your problem shift to another type

## Cassandra

> No single point of failure

- It doesn't have a single point-of-failure since it doesn't have a master node.
- It has the same underneath schema and structure like hbase
- Cassandra has a query language called `CQL`.
- CAP Theorem - consistency, availability & partition tolerance. you can only have 2 out of 3.
- Cassandra favors `availability` over `consistency`. Its traded with `tunable consistency` where we can adjust this with availability and consistency, `eventual consistency` all will not see the changes immediately it will take some time. We need `partition-tolerance` since we will be working with distributed system so its a given, so we can only choose one between availability and `consistency`.

![CAP theorem](./docs/04.png)

- Cassandra has a ring like architecture, it uses something like `gossip protocol`. Where every node talks to each other so any client can talk to any node.
- It uses consistent hashing to find the which node handle that `id`.

![cassandra architecture](./docs/05.png)

### Spark with Cassandra

- Look into this for cassandra [installation in cluster](./Section6-45%20InstallingCassandra.txt)
- `DataStax` offers a Spark-Cassandra connector - Allows you to read and write Cassandra tables as DataFrames
- Is smart about passing queries on those DataFrames down to the appropriate level

- Use cases
	- Use Spark for analytics on data stored in Cassandra
	- Use Spark to transform data and store it into Cassandra for transactional use

### Python with Spark + Cassandra

> Look into [CassandraSpark](./CassandraSpark.py)

- We're going to write into a table and query it with Spark
## MongoDB
