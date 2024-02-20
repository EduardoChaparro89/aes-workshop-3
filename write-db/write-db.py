from utils.utils import RabbitMQ
import time
import os

class CallBack:
    def __init__(self, rabbit) -> None:
        self.rabbit = rabbit
    
    def cb(self, ch, method, properties, body):
        """function to receive the message from rabbitmq
        print it
        sleep for 2 seconds
        ack the message"""

        print('to write on DB : ', body.decode('utf-8'))
        time.sleep(2)
        ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    rabbit = RabbitMQ(amqp_url = os.environ['AMQP_URL'])
    rabbit.subscribe('filtered-messages', CallBack(rabbit).cb)
