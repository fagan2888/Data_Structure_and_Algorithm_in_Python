import time
import random


class Sender:
    def __init__(self, freq=1):
        self._freq = freq

    def send_mail(self, sendto, times=None):
        if times is None:
            while True:
                k = random.random()
                print('sending... ', k)
                sendto.send(k)
                yield
                time.sleep(self._freq)
        else:
            for _ in range(times):
                k = random.random()
                print('sending... ', k)
                sendto.send(k)
                yield
                # time.sleep(self._freq)


class Checker:
    def __init__(self):
        pass

    def check_mail(self, sendto):
        while True:
            res = yield
            if res:
                print('checking... ', res)
                sendto.send(res)
                yield


class Receiver:
    def __init__(self):
        pass

    def receive_mail(self):
        while True:
            out = yield
            if out:
                print('receiving... ', out)
                print('deleted ', out)


if __name__ == "__main__":
    alice = Sender(5)
    checker = Checker()
    bob = Receiver()
    b_recv = bob.receive_mail()
    b_recv.send(None)
    check_gen = checker.check_mail(b_recv)
    check_gen.send(None)
    send_gen = alice.send_mail(check_gen)
    send_gen.send(None)

    while True:
        print('===')
        a = send_gen.send(None)
        # ca = check_gen.send(a)
        # b_recv.send(ca)
        # b_recv.send(check_gen.send(next(send_gen)))
        time.sleep(2)
