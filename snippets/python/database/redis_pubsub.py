import redis; r=redis.StrictRedis(); r.publish('read', 'data')
import redis; p=redis.StrictRedis().pubsub(ignore_subscribe_messages=True); p.subscribe('read'); [print(m) for m in p.listen()]
