# subscriber.py
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe("notifications", "alerts")  # iki kanala abone ol

print("Dinleniyor... (Ctrl+C ile çık)")

for message in pubsub.listen():
    if message["type"] == "message":
        print(f"[{message['channel']}] → {message['data']}")