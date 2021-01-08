""" Example use of Progress class """

import subprocess
import sys

import ffpbar


def run(command):
    progress = ffpbar.Progress()
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               universal_newlines=True,
                               encoding='utf-8')

    # reading the output log line by line and passing to _percent
    for out in process.stdout:
        progress.display(out.strip(), display_log=False)

    code = process.wait()
    if code:
        progress.clear()


if __name__ == "__main__":
    run(sys.argv[1:])
