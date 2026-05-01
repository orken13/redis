# redis_demo.py
import redis
import json
import time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# ──────────────────────────────────────────
# 1. STRING — Cache örneği
# ──────────────────────────────────────────
def demo_cache():
    print("\n── STRING / CACHE ──")

    r.setex("weather:istanbul", 10, json.dumps({"temp": 22, "condition": "Sunny"}))

    cached = r.get("weather:istanbul")
    print("Cache'den oku:", json.loads(cached))
    print("TTL:", r.ttl("weather:istanbul"), "sn")

# ──────────────────────────────────────────
# 2. HASH — Kullanıcı nesnesi
# ──────────────────────────────────────────
def demo_hash():
    print("\n── HASH / USER ──")

    r.hset("user:1", mapping={
        "name": "Emel",
        "email": "emel@example.com",
        "role": "engineer"
    })

    print("Tüm alanlar:", r.hgetall("user:1"))
    print("Sadece name:", r.hget("user:1", "name"))

    r.hset("user:1", "role", "senior engineer")
    print("Güncellendi:", r.hget("user:1", "role"))

# ──────────────────────────────────────────
# 3. LIST — Task queue
# ──────────────────────────────────────────
def demo_list():
    print("\n── LIST / QUEUE ──")

    # Kuyruğa iş ekle
    r.rpush("task_queue", "email_gonder", "rapor_olustur", "cache_temizle")

    print("Kuyruk uzunluğu:", r.llen("task_queue"))

    # İşleri sırayla al (FIFO)
    while r.llen("task_queue") > 0:
        task = r.lpop("task_queue")
        print("İşleniyor:", task)

# ──────────────────────────────────────────
# 4. SORTED SET — Leaderboard
# ──────────────────────────────────────────
def demo_sorted_set():
    print("\n── SORTED SET / LEADERBOARD ──")

    r.zadd("leaderboard", {
        "alice": 1500,
        "bob": 2300,
        "emel": 3100,
        "dave": 1800
    })

    # Yüksekten düşüğe sırala
    top = r.zrevrange("leaderboard", 0, -1, withscores=True)
    print("Sıralama:")
    for i, (name, score) in enumerate(top, 1):
        print(f"  {i}. {name} — {int(score)} puan")

    # Belirli kişinin sırası
    rank = r.zrevrank("leaderboard", "emel")
    print(f"Emel'in sırası: {rank + 1}")

# ──────────────────────────────────────────
# 5. INCR — Rate limiter (basit)
# ──────────────────────────────────────────
def demo_rate_limit():
    print("\n── INCR / RATE LIMIT ──")

    key = "rate:192.168.1.1"
    r.delete(key)  # temiz başla

    LIMIT = 3

    for i in range(5):
        count = r.incr(key)
        r.expire(key, 60)

        if count > LIMIT:
            print(f"İstek {i+1}:  Rate limit aşıldı ({count}/{LIMIT})")
        else:
            print(f"İstek {i+1}:  İzin verildi ({count}/{LIMIT})")

# ──────────────────────────────────────────
if __name__ == "__main__":
    r.flushdb()  # temiz başlangıç (dikkat: tüm veriyi siler)

    demo_cache()
    demo_hash()
    demo_list()
    demo_sorted_set()
    demo_rate_limit()