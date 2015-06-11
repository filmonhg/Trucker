from kafka import KafkaConsumer

# To consume messages
#consumer = KafkaConsumer("filmon-topic2",group_id="my_group",bootstrap_servers=["ec2-52-8-194-192.us-west-1.compute.amazonaws.com:9092"])
consumer = KafkaConsumer("filmon-topic2",group_id="my_group")
#for message in consumer:
    # message value is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
 #   print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         #message.offset, message.key,
                                         #message.value))

#kafka.close()
