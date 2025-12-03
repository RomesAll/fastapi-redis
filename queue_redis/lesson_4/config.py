from pika import BlockingConnection, PlainCredentials, ConnectionParameters
RMQ_HOST = '0.0.0.0'
RMQ_PORT = 5672
RMQ_USER = 'guest'
RMQ_PSW = 'guest'

connection_parametrs = ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=PlainCredentials(username=RMQ_USER, password=RMQ_PSW)
)

def get_connection() -> BlockingConnection:
    return BlockingConnection(parameters=connection_parametrs)