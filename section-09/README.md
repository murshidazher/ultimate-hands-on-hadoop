# Real-time Streaming

- Sometimes you might need to process data as the data is coming in and not sitting there in the cluster.

## Kafka

- Kafka is a general-purpose publish/subscribe messaging system
- Kafka servers store all incoming messages from publishers fro some period of time, and publishes them to a stream of data called a topic
- Kafka consumers subscribe to one or more topics, and receive data as it's published
- A stream / topic can have many different consumers, all with their own position in the steam maintained
- It's not just for Hadoop
- Kafka uses zookeeper for maintaining which topics and available and who subscribe to it.

### Example Kafka

> The implementation details is available [here](./Section9-76PublishingWebLogsWithKafka.txt)

- We will write all the logs from different servers and aggregate it to a single file using kafka as new logs comes in under the same topic.
- This is similar to publishing web logs.

## Flume
