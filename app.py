# app.py
from redis_client import RedisClient

def servis_a():
    r = RedisClient().get_client()
    r.set("servis_a", "çalışıyor")
    print("Servis A:", r.get("servis_a"))

def servis_b():
    r = RedisClient().get_client()
    r.set("servis_b", "çalışıyor")
    print("Servis B:", r.get("servis_b"))

def servis_c():
    r = RedisClient().get_client()
    print("Servis C okudu:", r.get("servis_a"), r.get("servis_b"))

# Her servis ayrı RedisClient() oluşturuyor ama
# aslında hepsi aynı instance'ı kullanıyor
servis_a()
servis_b()
servis_c()

# Singleton kontrolü
a = RedisClient()
b = RedisClient()
print("\nAynı instance mı?", a is b)  # True