import time
from typing import TYPE_CHECKING
import logging

from config import get_connection, MQ_EXCHANGE, MQ_ROUTING_KEY

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel

def produce_massage(channel: "BlockingChannel", indx:int):
    message = f'hello world {indx}'
    print(message)
    # time.sleep(1)
    channel.basic_publish(exchange=MQ_EXCHANGE, routing_key=MQ_ROUTING_KEY, body=message)

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue=MQ_ROUTING_KEY)
            for i in range(1, 11):
                produce_massage(ch, i)

if __name__ == "__main__":
    main()