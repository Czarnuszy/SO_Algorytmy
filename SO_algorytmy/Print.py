import time
import progressbar


def process_print(bust):
    bar = progressbar.ProgressBar()
    for i in bar(range(bust)):
        time.sleep(1)
