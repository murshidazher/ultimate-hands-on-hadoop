import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

# regex to parse, pattern match and extract an apache web server log line
parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

def extractURLRequest(line):
    exp = pattern.match(line)
    if exp:
        request = exp.groupdict()["request"]
        if request:
           requestFields = request.split()
           if (len(requestFields) > 1):
                return requestFields[1]


if __name__ == "__main__":

    sc = SparkContext(appName="StreamingFlumeLogAggregator")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)

    # FlumeUtils has all the modules to work spark with flume
    # this is a push model where pushing the data from one flume agent into another as far as flume is concerned
    # we can also set up a pull model where we can set up a custom sink within flume to and establish a bi-directional relationship between flume and spark streaming and its more robust way of handling this if we're doing this in real production.
    flumeStream = FlumeUtils.createStream(ssc, "localhost", 9092) # we configured the port in sparkstreamingflume.conf

    lines = flumeStream.map(lambda x: x[1])
    urls = lines.map(extractURLRequest)

    # Reduce by URL over a 5-minute window sliding every second of slide/compute interval
    urlCounts = urls.map(lambda x: (x, 1)).reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y : x - y, 300, 1)

    # Sort and print the results
    sortedResults = urlCounts.transform(lambda rdd: rdd.sortBy(lambda x: x[1], False))
    sortedResults.pprint()

    # whenever we're doing a windowed operation we need to maintain the state somewhere, so that if something fails then we can restart the job and continue from where we left off.
    ssc.checkpoint("/home/maria_dev/checkpoint")
    ssc.start()
    ssc.awaitTermination()
