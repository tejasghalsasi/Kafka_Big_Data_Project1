# Kafka_Big_Data_Project

Apache Kafka® is a distributed streaming platform. 

A streaming platform has three key capabilities:

Publish and subscribe to streams of records, similar to a message queue or enterprise messaging system.


Store streams of records in a fault-tolerant durable way.


Process streams of records as they occur.



Kafka is generally used for two broad classes of applications:

Building real-time streaming data pipelines that reliably get data between systems or applications

Building real-time streaming applications that transform or react to the streams of data

More information here: https://kafka.apache.org/intro

# Project Description:

The application I have made is a python program to read line by line a txt file of "The Merchant of Venice" by William Shakespeare and feed it to producer.

(The txt file can be downloaded from here: http://www.gutenberg.org/cache/epub/2243/pg2243.txt)

The topic name of this producer is Merchant

The consumer will be listening for the topic and will print it as soon as the producer produces the content

