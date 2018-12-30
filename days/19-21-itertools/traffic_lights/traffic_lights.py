import itertools
import time
import random

yellow_duration=1
duration=1
colors = 'Green Yellow Red'.split()
rotation=itertools.cycle(colors)
while True:
    color=next(rotation)
    if color=='Yellow':
        duration=yellow_duration
    elif color=='Red':
        duration=random.randint(1,3)

    print(f'{color} - {duration} seconds')
    time.sleep(duration)
