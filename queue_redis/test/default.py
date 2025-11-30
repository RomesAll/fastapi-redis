import pika
RMQ_HOST = "0.0.0.0"
RMQ_PORT = 5672

RMQ_USER = "guest"
RMQ_PASSWORD = "guest"

def get_conn():
    return pika.BlockingConnection(pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD)))

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

with get_conn() as conn:
    with conn.channel() as ch:
        ch.queue_declare(queue='q1')
        ch.basic_publish(exchange='', routing_key='q1', body='hello world111')
        

a = input()

with get_conn() as conn:
    with conn.channel() as ch:
        ch.queue_declare(queue='q1')
        ch.basic_consume(queue='q1', auto_ack=True, on_message_callback=callback)
        ch.start_consuming()
