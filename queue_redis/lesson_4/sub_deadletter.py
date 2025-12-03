from config import *
import time

def processing_massage(channel, method, properties, body: bytes):
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.exchange_declare(exchange='dev-exc-dl', exchange_type='direct', durable=True)
            queue_dl = ch.queue_declare(queue='dev-queue-dl', durable=True)
            ch.queue_bind(queue=queue_dl.method.queue, exchange='dev-exc-dl', routing_key='def-message-key-dl')
            ch.basic_consume(queue=queue_dl.method.queue, on_message_callback=processing_massage, auto_ack=False)
            ch.start_consuming()

if __name__ == '__main__':
    main()