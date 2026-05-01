# redis_client.py
import redis

class RedisClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Redis bağlantısı kuruluyor...")
            cls._instance = super().__new__(cls)
            cls._instance.client = redis.Redis(
                host="localhost",
                port=6379,
                decode_responses=True,
                connection_pool=redis.ConnectionPool(
                    host="localhost",
                    port=6379,
                    decode_responses=True,
                    max_connections=10  # aynı anda max 10 bağlantı
                )
            )
        return cls._instance

    def get_client(self):
        return self.client