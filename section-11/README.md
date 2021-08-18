# Other technologies

## Impala

- Cloudera alternative to `Hive`
- Massive Parallel SQL engine on Hadoop
- Impala is always running, so you avoid the start-up costs when starting a Hive query
  - Impala is made for `BI-style` queries
- Bottom line: Impala's often faster than Hive, but Hive offers more versatility
- Consider using Impala instead of Hive if you are using Cloudera

## Accumulo

> Like HBase with better security. a NoSQL database.

- Another BigTable clone (like `HBase`)
- But offers a better security model
  - `Cell-based access control` - Tightly control who can see what data
- And server-side programming
- Consider it for your NoSQL needs if you have complex security requirements
- But make sure the systems that need to read this data can talk to it.

## Redis

> `memcache` can only store key-value pair while Redis can store whole range of data structures.

- A distributed in-memory data store (like `memcache`)
- But it's more than a cache
- Good support for storing data structures
- Can persist data to disk
- Can be used as a data store and not just a cache
- Popular caching layer for web apps

## Ignite

> This is an alternative to `redis`.

- An `in-memory data fabric`
- Think of it as an alternative to Redis
- But it's closer to a database
  - `ACID` guarantees - ex. for financial transaction
  - SQL support
  - But it's all done in-memory

## Elasticsearch

- A distributed document search and analytics engine
- Really popular
- Wikipedia, The Guardian, Stack Overflow, many more
- Can handle things like real-time search-as-you-type
- When paired with `Kibana`, great for interactive exploration
- Amazon offers an Elasticsearch Service
