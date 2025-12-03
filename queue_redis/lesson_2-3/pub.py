from config import *
import string, random

def create_message(i: int):
    message = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    return message + ' ' + str(i)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.exchange_declare(exchange='dev-exc', exchange_type='fanout', durable=True)
            # ch.queue_declare(queue='new_queue')
            # ch.queue_bind(queue='new_queue', exchange='dev-exc')
            for i in range(10):
                ch.basic_publish(exchange='dev-exc', routing_key='', body=create_message(i))

if __name__ == '__main__':
    main()