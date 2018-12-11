import redis

pool = redis.ConnectionPool(host='myredis', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

