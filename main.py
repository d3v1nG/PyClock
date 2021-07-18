from ChessTimer import ChessTimer
import time


def done():
    print("Time up")

timer = ChessTimer(2)
print(timer.get_remaining_time())
timer.start()

time.sleep(5)

timer.pause()

print(timer.get_remaining_time())

