import redis
import time, json

connection = redis.Redis(
	port=6379, # стандартный порт для подключения к Redis без SSL
	db=0,
	decode_responses=True # ответы сервера Redis будут автоматически декодироваться в читаемый вид
)

queue = connection.pubsub() # создаем очередь типа Pub/Sub
queue.subscribe("channelFirst", "channelSecond") # подписываемся на указанные каналы

# бесконечный цикл обработки очереди сообщений
while True:
	time.sleep(0.1)
	msg = queue.get_message() # извлекаем сообщение
	if msg: # проверяем сообщение на пустоту
		if not isinstance(msg["data"], int): # проверяем, какой тип информации хранится в переменной data (msg имеет тип словаря)
			print(msg["data"]) # выводим сообщение в консоль