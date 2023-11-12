"""tests reading from redis"""
import redis
import os

def lambda_handler(event, context):
    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']
    r = redis.Redis(host=redis_host, port=redis_port)

    return {"res": r.get("my cached key")}
