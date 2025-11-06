from redis import Redis
from rq import SimpleWorker, Queue

if __name__ == "__main__":
    queue = Queue(connection=Redis(
        host="localhost",
        port="6379"
    ))

    worker = SimpleWorker([queue], connection=queue.connection)
    worker.work(burst=True)
