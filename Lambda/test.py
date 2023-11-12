"""tests reading from redis"""
import redis
import os

def lambda_handler(event, context):
    print("starting lambda")
    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']
    r = redis.Redis(host=redis_host, port=redis_port)
    print(r.ping())

    return {"res": r.get("my cached key")}
