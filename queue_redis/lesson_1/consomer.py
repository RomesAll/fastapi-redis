import time
from typing import TYPE_CHECKING
import logging

from config import (
    get_connection,
    configure_logging,
    MQ_ROUTING_KEY,
)

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel
    from pika.spec import Basic, BasicProperties

# log = logging.getLogger(__name__)


# def process_new_message(
#     ch: "BlockingChannel",
#     method: "Basic.Deliver",
#     properties: "BasicProperties",
#     body: bytes):

#     # 1/0
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#     print(body)
#     print(properties)


# def consume_messages(channel: "BlockingChannel") -> None:
#     channel.basic_consume(
#         queue=MQ_ROUTING_KEY,
#         on_message_callback=process_new_message,
#         # auto_ack=True,
#     )
#     log.warning("Waiting for messages...")
#     channel.start_consuming()
#     print('aa')


# def main():
#     configure_logging(level=logging.WARNING)
#     with get_connection() as connection:
#         log.info("Created connection: %s", connection)
#         with connection.channel() as channel:
#             log.info("Created channel: %s", channel)
#             consume_messages(channel=channel)
#     print('bbb')

def process_new_message(ch: "BlockingChannel", method: "Basic.Deliver", prop: "BasicProperties", body: bytes):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body)

def consume_messages(channel: "BlockingChannel"):
    channel.basic_consume(queue=MQ_ROUTING_KEY, on_message_callback=process_new_message, auto_ack=False)
    channel.start_consuming()

def main():
    with get_connection() as conn:
        with conn.channel() as ch:
            consume_messages(ch)

if __name__ == "__main__":
    main()