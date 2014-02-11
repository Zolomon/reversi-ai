import datetime
import queue
import threading


class TestThread(threading.Thread):
    def __init__(self, mutex, q, end_time):
        self.mutex = mutex
        self.q = q
        self.start_time = datetime.datetime.now()
        self.end_time = end_time
        print("Created thread")
        threading.Thread.__init__(self)

    def run(self):
        print("Starting thread")
        self.process_data(self.q)
        print("Exiting")

    def process_data(self, q):
        print("Loading ")
        while self.start_time < self.end_time:
            with self.mutex:
                self.start_time = datetime.datetime.now()

        with self.mutex:
            q.put((1, 1))


def main():
    stdoutmutex = threading.Lock()
    workQueue = queue.Queue(1)
    threads = []

    t = TestThread(stdoutmutex, workQueue,
                   datetime.datetime.now() + datetime.timedelta(seconds=5))
    t.start()
    threads.append(t)

    for t in threads:
        t.join()

    print(workQueue.get())


if __name__ == '__main__':
    main()