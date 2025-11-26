'''
Урок 5: https://www.youtube.com/watch?v=KMY7uZmpdwA&list=PLF4MWzDJPFSbY5TxSdq3DMPSL7ke51u93&index=5
'''

import redis, sqlite3, json

def test():
    rediscli = redis.Redis()

    # Хранение данных в формате json
    data = 'hello aaa puipa'
    rediscli.set('data', json.dumps(data)) # Преобразование в json
    res = json.loads(rediscli.get('data')) # Преобразование в пит. объекты
    print(res)

    data_new = [1, 2, 3, 'aboba aaa']
    rediscli.set('data_new', json.dumps(data_new))
    res = json.loads(rediscli.get('data_new'))
    print(res)

    rediscli.close()

