from pyzbar.pyzbar import decode
import redis
import os

def lambda_handler(event, context):
    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']
    r = redis.Redis(host=redis_host, port=redis_port)

    barcode = decode(event['image'])
    if not barcode:
        return {"response": "No barcode detected"}
    else:
        for b in barcode:
            if b.data!="":
                number = b.data.decode('utf-8')
                break
        action = r.get(number)
        return {"response": action}
