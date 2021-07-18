from threading import Timer
import time


class ChessTimer:

    def __init__(self, timeout):
        timeout = timeout * 60
        self.timer = Timer(timeout, self.end)

        self.start_time = None
        self.cancel_time = None

        # Used for creating a new timer upon renewal
        self.timeout = timeout
        self.callback = self.end

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.start_time = time.time()
        self.timer.start()

    def pause(self):
        self.cancel_time = time.time()
        self.timer.cancel()
        return self.get_remaining_time()

    def resume(self):
        self.timeout = self.get_remaining_time()
        self.timer = Timer(self.timeout, self.callback)
        self.start_time = time.time()
        self.timer.start()

    def get_remaining_time(self):
        if self.start_time is None or self.cancel_time is None:
            return self.convert_time(self.timeout)
        return self.convert_time(self.timeout - (self.cancel_time - self.start_time))


    def convert_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return str("{0}:{1}".format(str(minutes), str(seconds)))
    
    def end(self):
        print("TIMES UP BITCH")
        return True