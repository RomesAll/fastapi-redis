'''
Урок 4: https://www.youtube.com/watch?v=KMY7uZmpdwA&list=PLF4MWzDJPFSbY5TxSdq3DMPSL7ke51u93&index=4
'''

import redis, sqlite3, json

def get_my_friends():
    connect = sqlite3.connect(database='database.db')
    cursor = connect.cursor()
    rediscli = redis.Redis()
    cache_value = rediscli.get("users")
    if cache_value is not None:
        data = json.loads(cache_value)
        return data
    
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    rediscli.set('users', json.dumps(result))
    cursor.close()
    rediscli.close()
    return result

get_my_friends()