import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

r.set("server:name", "fido")
print("server:name => {}".format(r.get("server:name")))
