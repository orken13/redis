# Redis Demo

Practical examples covering Redis fundamentals and advanced patterns in Python.

---

## Setup

```bash
# Start Redis with Docker
docker run -d -p 6379:6379 --name redis redis

# Install dependencies
pip3 install redis --break-system-packages
```

---

## Files

### `main.py` — Core Data Types

Covers the 5 essential Redis structures.

| Type | Purpose | Example Use Case |
|------|---------|-----------------|
| **String** | Store a single value with optional TTL | Caching API responses |
| **Hash** | Store an object with multiple fields | User profile data |
| **List** | Ordered list, FIFO/LIFO | Task queue |
| **Sorted Set** | Ranked collection by score | Leaderboard |
| **INCR** | Atomic counter | Rate limiting |

```bash
python3 redis_demo.py
```

---

### `pipeline.py` — Pipeline

By default, every Redis command makes a separate network round-trip. With a pipeline, commands are sent in bulk — significantly faster.

```
Without pipeline → 1000 commands = 1000 network requests
With pipeline    → 1000 commands = 1 network request
```

```bash
python3 pipeline_demo.py
```

---

### `subscriber.py` + `publisher.py` — Pub/Sub

One side publishes messages, the other side listens. Used when services need to react to events in real time.

```
publisher → "notifications" channel → subscriber receives → prints to console
```

```bash
# Terminal 1
python3 subscriber.py

# Terminal 2
python3 publisher.py
```

---

### `redis_client.py` + `app.py` — Connection Pool + Singleton

Opening `redis.Redis()` everywhere creates a new connection each time — expensive. The Singleton pattern ensures only **one** Redis instance exists across the app. The Connection Pool manages multiple concurrent requests efficiently.

```
Singleton        → single Redis instance throughout the app
Connection Pool  → up to 10 concurrent connections, reused automatically
```

```bash
python3 app.py
```

---

## Summary

```
main.py      → String, Hash, List, Sorted Set, Rate Limiting
pipeline.py   → Bulk command execution (performance optimization)
subscriber.py      → Channel listener
publisher.py       → Channel publisher
redis_client.py    → Singleton + Connection Pool setup
app.py             → Singleton usage example
```
