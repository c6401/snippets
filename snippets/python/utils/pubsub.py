class PubSub:
    def __init__(self):
        self.subscribers = []

    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber(message)

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
