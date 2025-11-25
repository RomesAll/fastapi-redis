'''
Урок 1: https://www.youtube.com/watch?v=oNz_uXjOCpo&list=PLF4MWzDJPFSbY5TxSdq3DMPSL7ke51u93&index=1
'''
import redis, time

client = redis.Redis(host='127.0.0.1', port=6379, db=0)

client.set(name='psw', value='qwerty', ex=5)

print(client.ttl(name='psw'))

print(client.get(name='psw'))

time.sleep(5)

print(client.get(name='psw'))

client.close()