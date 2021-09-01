from os import startfile
from pynput.keyboard import Key, Listener
from ChessTimer import ChessTimer

# for future expandibility
class GameManager:
    def __init__(self, time) -> None:
        self.time = time
        self.p1_timer = ChessTimer(time)
        self.p2_timer = ChessTimer(time)
        self.started = False
        # with Listener(on_press = self.start) as listener:   
        #     listener.join()

    def start(self, key):
        # start the game
        if self.started == False:
            if key==Key.shift:
                self.p1_timer.start()
                self.p2_timer.start()
                self.p2_timer.pause()
            elif key==Key.shift_r:
                self.p2_timer.start()
                self.p1_timer.start()
                self.p1_timer.pause()
            self.started = True
        # main game clock
        if self.started:
            if key==Key.shift:
                self.p2_timer.pause()
                self.p1_timer.resume()
            elif key==Key.shift_r:
                self.p1_timer.pause()
                self.p2_timer.resume()


    def reset(self):
        pass