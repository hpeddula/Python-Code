import threading
class Demo(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
send = Demo(name='Sending Messages')
receive = Demo(name='Receving Messages')
send.start()
receive.start()
