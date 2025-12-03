from config import *
import time

def processing_massage(channel, method, properties, body: bytes):
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.exchange_declare(exchange='dev-exc', exchange_type='fanout', durable=True)
            queue = ch.queue_declare(queue='', exclusive=True)
            ch.queue_bind(queue=queue.method.queue, exchange='dev-exc')
            ch.basic_consume(queue=queue.method.queue, on_message_callback=processing_massage, auto_ack=False)
            ch.start_consuming()

if __name__ == '__main__':
    main()