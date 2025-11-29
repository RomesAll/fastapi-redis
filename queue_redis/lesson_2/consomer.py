import time
from typing import TYPE_CHECKING
import logging
from config import get_connection, MQ_ROUTING_KEY

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel
    from pika.spec import Basic, BasicProperties

def process_new_message(ch: "BlockingChannel", method: "Basic.Deliver", prop: "BasicProperties", body: bytes):
    number = body.split()[2]
    if int(number) % 2 == 0:
        time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body)

def consume_messages(channel: "BlockingChannel"):
    channel.basic_qos(prefetch_count=1) # Выдача сообщений по одному за раз свободному потребителю
    channel.basic_consume(queue=MQ_ROUTING_KEY, on_message_callback=process_new_message, auto_ack=False)
    channel.start_consuming()

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            consume_messages(ch)

if __name__ == "__main__":
    main()