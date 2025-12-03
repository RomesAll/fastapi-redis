import pika, uvicorn, time, asyncio
from fastapi import FastAPI

app = FastAPI()

def task():
    for i in range(10):
        print(i)
        time.sleep(5)

@app.get('/test')
def test():
    task()
    return {'message': 'ok'}

@app.get('/test1')
def test1():
    task()
    return {'message': 'ok'}

if __name__ == '__main__':
    uvicorn.run('pub:app', reload=True)