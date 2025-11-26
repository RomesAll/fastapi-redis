'''
Урок 3: https://www.youtube.com/watch?v=T5aioQMueaA&list=PLF4MWzDJPFSbY5TxSdq3DMPSL7ke51u93&index=3
'''

import json
import redis
# FLUSHALL удалить все ключи из всех бд
# FLUSHDB удалить все ключи из выбранной бд

# with redis.Redis() as client:
#     elements = client.lrange('massive', 0, -1) # Вывести получить список элементов
#     client.lpush('massive', 'number1') # Добавить слево
#     client.lpush('massive', 'number2') # Добавить слево
#     client.lindex('massive', 3) # Вывести элемент по индексу
#     print(elements)

with redis.Redis() as client:
    client.hset(name='roman', mapping={'old': '23', 'second_name': 'beskokotov', 'color_eyes': 'blue'})
    client.hset(name='roman', mapping={'aa': '24'})
    client.expire(name='roman', time=10)

    # user = client.hgetall('roman')
    # user = {k.decode('utf-8'):v.decode('utf-8') for k,v in user.items()}
    # if isinstance(user, dict) and isinstance(list(user.keys())[0], str):
    #     print('yes')