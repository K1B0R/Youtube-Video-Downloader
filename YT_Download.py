from pytube import YouTube
import colorama
import sys
import time
import threading
import itertools
from colorama import init, Fore, Back, Style

init(autoreset=True)

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done = True

print('[=] Please Enter THe Url Of The Video That You Want To Download!')

time.sleep(1)
print('\n')
url = input('URL: ')

YouTube(url).streams.first().download()