import redis

pool = redis.ConnectionPool(host='myredis', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

count = r.incr('test:counts')
print("test:counts => {}".format(count))
