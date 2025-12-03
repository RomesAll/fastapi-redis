from config import *
import string, random

def create_message(i: int):
    message = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    return message + ' ' + str(i)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.exchange_declare(exchange='exc', exchange_type='direct', durable=True)
            queue = ch.queue_declare(queue='queue', durable=True, arguments={'x-dead-letter-exchange':'dlx'})
            ch.queue_bind(queue=queue.method.queue, exchange='exc', routing_key='')
            
            for i in range(30):
                ch.basic_publish(exchange='exc', routing_key='', body=create_message(i))

if __name__ == '__main__':
    main()