# publisher.py
import redis
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

messages = [
    ("notifications", "Yeni kullanıcı kaydoldu"),
    ("alerts", "Disk doluluk %90 aşıldı"),
    ("notifications", "Sipariş tamamlandı"),
    ("alerts", "API yanıt süresi yüksek"),
]

for channel, msg in messages:
    print(f"Gönderiliyor → [{channel}]: {msg}")
    r.publish(channel, msg)
    time.sleep(1)