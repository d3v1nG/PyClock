from threading import Timer
import time


class ChessTimer:
    # simple timer class wrapped around threading.Timer
    # Todo: Format time for tkinter
    def __init__(self, initial_start_time):
        # convert into seconds
        initial_start_time = initial_start_time * 60
        self.timer = Timer(initial_start_time, self.end)

        self.start_time = None
        self.cancel_time = None
        # Used for creating a new timer upon renewal
        self.timeout = initial_start_time

        self.running = False
        self.over = True    

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.start_time = time.time()
        # create new timer, instead of trying to start old thread
        self.timer = Timer(self.timeout,self.end)
        self.running = True
        self.over = False

    def pause(self):
        if self.running:
            self.cancel_time = time.time()
            self.cancel()
            self.running = False
            self.timeout = self.get_remaining_time()
            

    def resume(self):
        if not self.running:
            self.timer = Timer(self.timeout, self.end)
            self.start_time = time.time()
            self.running = True

    def get_remaining_time(self):
        if self.start_time is None or self.cancel_time is None:
            return self.timeout
        else:
            return ( self.timeout - (self.cancel_time - self.start_time) )

    def get_time_live(self):
        if self.running:
            self.pause()
            self.resume()
            return self.get_clock()

    def convert_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        # not good programming but fuck it
        if seconds == 0:
            return str("{0}:{1}".format(str(round(minutes)), "00"))
        elif round(seconds) == 60:
            return str("{0}:{1}".format(str(round(minutes)), "59"))
        return str("{0}:{1}".format(str(round(minutes)), str(round(seconds))))

    def get_clock(self):
        return self.convert_time(self.get_remaining_time())
    
    def end(self):
        print("TIMES UP BITCH")
        self.over = True