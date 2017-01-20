import time
import progressbar


def process_print(bust):
    bar = progressbar.ProgressBar(widgets=None)
    for i in bar(range(bust)):
        time.sleep(1)

from tqdm import tnrange, tqdm_notebook
from time import sleep

for i in tnrange(10, desc='1st loop'):
    for j in tqdm_notebook(xrange(100), desc='2nd loop'):
        sleep(0.01)