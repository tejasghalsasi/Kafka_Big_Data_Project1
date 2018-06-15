#this is a producer file which prints the whole Merchent of Venice Line-by-Line
#Before next line is printed there is a pause of 0.5 seconds
import threading, logging, time
from kafka import KafkaProducer
from kafka.errors import KafkaError



        

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic = "Merchant"
topic2="my-topic" 
producer.send(topic, b"Lets get Started")
with open ("/home/tg/Desktop/GIT_Folder/Kafka_Big_Data_Project1/merchant.txt", "r") as myfile:
    data = myfile.readlines()
    for line in data:
        producer.send(topic,line)
        producer.send(topic2,'This is a sample message for topic 2')
        time.sleep(0.5) 
producer.close()