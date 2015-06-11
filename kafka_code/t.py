from kafka import KafkaConsumer

consumer=KafkaConsumer("my-topic",group_id="my_group",bootstrap_servers=["localhost:9092"])
