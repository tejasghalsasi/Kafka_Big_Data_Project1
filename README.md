# Kafka_Big_Data_Project

# Project Description:

The application I have made is a python program to read line by line a txt file of "The Merchant of Venice" by William Shakespeare and feed it to producer.

(The txt file can be downloaded from here: http://www.gutenberg.org/cache/epub/2243/pg2243.txt)

The topic name of this producer is Merchant

The consumer will be listening for the topic and will print it as soon as the producer produces the content

# Adding more than 1 topic:

The screenshot shows 2 listeners.

[https://github.com/tejasghalsasi/Kafka_Big_Data_Project1/blob/master/Screenshot%20from%202018-06-15%2002-16-02.png]


Prior to the execution of Shakespeare txt file, I had passed a video along with a part of the text file to the Topic "my-topic"

The screenshot shows the two topics and the producer window.

For more information please check out my video on youtube.

https://youtu.be/FL6LIq_kGGk




# What is Kafka?

Apache Kafka® is a distributed streaming platform. 

A streaming platform has three key capabilities:

Publish and subscribe to streams of records, similar to a message queue or enterprise messaging system.


Store streams of records in a fault-tolerant durable way.


Process streams of records as they occur.



Kafka is generally used for two broad classes of applications:

Building real-time streaming data pipelines that reliably get data between systems or applications

Building real-time streaming applications that transform or react to the streams of data

More information here: https://kafka.apache.org/intro

