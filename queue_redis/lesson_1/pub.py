from config import *
import string, random

def create_message(i: int):
    message = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    return message + ' ' + str(i)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='new_queue')
            for i in range(10):
                ch.basic_publish(exchange='', routing_key='new_queue', body=create_message(i))

if __name__ == '__main__':
    main()