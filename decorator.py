import redis, hashlib, json

def cache(exp=60):
    def inner_decorators(func):
        def wrapped(*args, **kwargs):
            key = str(func.__name__) + ''.join([str(i) for i in args]) + ''.join({str(v) for k,v in kwargs.items()})
            hash_object = hashlib.sha256(key.encode())
            hash_key = hash_object.hexdigest()
            with redis.Redis() as client:
                value = client.get(name=hash_key)
                if value is None:
                    response = func(*args, **kwargs)
                    client.set(name=hash_key, value=json.dumps(response), ex=exp)
                    return response
                return json.loads(value)
        return wrapped
    return inner_decorators


@cache(exp=20)
def test(a = 1,b = 2):
    return a + b

a = test(2, 4)
print(a)
test(2, 4)