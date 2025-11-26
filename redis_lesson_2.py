'''
Урок 2: https://www.youtube.com/watch?v=49Je2gsonyM&list=PLF4MWzDJPFSbY5TxSdq3DMPSL7ke51u93&index=2

'''

import redis, time, random, string
# string.ascii_letters

with redis.Redis() as client:
    for i in range(10):
        client.set(name=''.join([random.choice(string.ascii_letters) for i in range(random.randint(7, 20))]), value='test')

with redis.Redis() as client:
    generator = client.scan_iter('*')
    print(next(generator))
    print(next(generator))
