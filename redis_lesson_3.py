'''
Урок 3: https://www.youtube.com/watch?v=T5aioQMueaA&list=PLF4MWzDJPFSbY5TxSdq3DMPSL7ke51u93&index=4

'''

import redis
# FLUSHALL удалить все ключи из всех бд
# FLUSHDB удалить все ключи из выбранной бд

with redis.Redis() as client:
    elements = client.lrange('massive', 0, -1) # Вывести получить список элементов
    client.lpush('massive', 'number1') # Добавить слево
    client.lpush('massive', 'number2') # Добавить слево
    client.lindex('massive', 3) # Вывести элемент по индексу
    print(elements)

