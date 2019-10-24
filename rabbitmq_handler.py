import pika

class RabbitMQHandler:
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()

    def declare_queue(self, queue):
        self.channel.queue_declare(queue=queue)

    def send_message(self, queue, message):
        self.channel.basic_publish(exchange='', routing_key=queue, body=message)

    def read_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return body.decode()
        else:
            print('No message returned.')

    def close(self):
        self.connection.close()

rabbitmq = RabbitMQHandler('localhost')

# Declare a queue
rabbitmq.declare_queue('my_queue')

# Send a message
rabbitmq.send_message('my_queue', 'Hello, World!')

# Read a message
message = rabbitmq.read_message('my_queue')
print(message)

# Close the connection
rabbitmq.close()
