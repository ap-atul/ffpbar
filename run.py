"""
Sample use of Progress class
"""

import sys
import subprocess
from lib.progress import Progress


def run(command):
    """
    running a FFmpeg command, this is designed for
    FFmpeg only, so it will work on it only.
    :param command: list
    :return: None
    """
    progress = Progress()
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               universal_newlines=True,
                               encoding='utf-8')

    # reading the output log line by line and passing to progress
    for out in process.stdout:
        progress.displayProgress(out.strip(), displayLog=True)

    code = process.wait()
    if code:
        progress.clear()


if __name__ == "__main__":
    run(sys.argv[1:])
