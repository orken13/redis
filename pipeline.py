# pipeline_demo.py
import redis
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# ── Pipeline OLMADAN (her komut ayrı network round-trip) ──
print("── Pipeline YOK ──")
start = time.time()

for i in range(1000):
    r.set(f"key:{i}", i)

print(f"Süre: {time.time() - start:.3f}s")

# ── Pipeline İLE (tüm komutlar tek seferde gönderilir) ──
print("\n── Pipeline VAR ──")
start = time.time()

pipe = r.pipeline()
for i in range(1000):
    pipe.set(f"key:{i}", i)
pipe.execute()  # hepsini tek seferde gönder

print(f"Süre: {time.time() - start:.3f}s")

# ── Gerçek kullanım örneği: kullanıcı kaydı ──
print("\n── Kullanıcı kaydı (pipeline) ──")

pipe = r.pipeline()
pipe.hset("user:42", mapping={"name": "Emel", "role": "engineer"})
pipe.sadd("active_users", "42")
pipe.incr("total_user_count")
pipe.expire("user:42", 3600)
results = pipe.execute()

print("Sonuçlar:", results)
print("Total user count:", r.get("total_user_count"))