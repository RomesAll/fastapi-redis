from config import *
import time

def processing_massage(channel, method, properties, body: bytes):
    print(body)
    message = body.decode()
    if int(message.split()[1]) % 2 == 0:
        time.sleep(5)
    else:
        time.sleep(1)

    channel.basic_ack(delivery_tag=method.delivery_tag)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='new_queue')
            ch.basic_qos(prefetch_count=1)
            ch.basic_consume(queue='new_queue', on_message_callback=processing_massage, auto_ack=False)
            ch.start_consuming()

if __name__ == '__main__':
    main()