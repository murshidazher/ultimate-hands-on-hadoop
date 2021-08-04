# Streaming

> Spark Streaming and Apache Storm

- We've seen in the [previous](./section-09/README.md) section on how to get the real time data into HDFS
- Now, in this section we need to know how to process that incoming data.
- Rather than analyzing it in batch manner for incoming streams of data, why can't we analyze them as they are coming in?

## Spark Streaming

- Spark streaming is not really real-time what it does is called `micro-batches` ex. like for `1sec` batches.
- `Dstream` is responsible for generating RDDs at batch intervals.
- Spark streaming job is different from batch processing in spark job is that we process using the `Dstream`.
- Windowed Transformation allows for analyzing microbatches greater than your single micro-batch limit.
- ex: top-sellers from the past hour
  - You might process data every one second (the batch interval)
  - But maintain a window of one hour
- Window `slides` as time goes on to represent batches within the window interval

![micro-batches spark streaming](./docs/01.png)
![Dstreams spark streaming](./docs/02.png)

## Apache Storm
