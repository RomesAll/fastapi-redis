from config import *
import time,  random
from pika.channel import Channel

def processing_massage(channel, method, properties, body: bytes):
    time.sleep(1)
    if random.random() > 0.5:
        channel.basic_ack(delivery_tag=method.delivery_tag)
        print('Message ack', body)
    else:
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        print('Message nack', body)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.exchange_declare(exchange='dlx', exchange_type='direct', durable=True)
            queue_dl = ch.queue_declare(queue='dlq', durable=True)
            ch.queue_bind(queue=queue_dl.method.queue, exchange='dlx', routing_key='')
            
            ch.basic_consume(queue='queue', on_message_callback=processing_massage, auto_ack=False)
            ch.start_consuming()

if __name__ == '__main__':
    main()