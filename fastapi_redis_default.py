from fastapi import FastAPI
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import uvicorn, asyncio

app = FastAPI()

@app.get('/get_data')
@cache(expire=60)
async def get_data():
    await asyncio.sleep(10)
    return 'Data'

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(url="redis://localhost", port=6379, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')

if __name__ == '__main__':
    uvicorn.run("fastapi_redis_default:app", reload=True)