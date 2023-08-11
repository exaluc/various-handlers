from confluent_kafka import Producer, Consumer, KafkaError

class KafkaHandler:
    def __init__(self, servers, group_id=None):
        self.servers = servers
        self.group_id = group_id

    def produce(self, topic, message):
        p = Producer({'bootstrap.servers': self.servers})
        p.produce(topic, message)
        p.flush()

    def consume(self, topic):
        c = Consumer({
            'bootstrap.servers': self.servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })

        c.subscribe([topic])

        while True:
            msg = c.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            print('Received message: {}'.format(msg.value().decode('utf-8')))

        c.close()


kafka = KafkaHandler('localhost:9092', 'my-group')

# Produce a message
kafka.produce('my-topic', 'Hello, World!')

# Consume messages
kafka.consume('my-topic')
