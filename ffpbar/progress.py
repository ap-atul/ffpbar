"""
This file defines the progress base from tqdm
and updates it according to the FFmpeg  logs based on
the time and duration in the logs
"""

from tqdm import tqdm

from .parser import Parser


class Progress:
    def __init__(self):
        """ Initializes the progress bar object """
        self.bar = tqdm(total=100)
        self.desc = tqdm(position=1, bar_format='{desc}')
        self.parser = Parser()
        self.progress = 0

    def display(self, log: str, display_log=False):
        """ Extracts the time and duration from log and update the progress bar"""
        self.desc.set_description(desc=log[0: 120], refresh=True)
        duration, time = self.parser.extract_time_duration(log)

        if time is not None:
            current_progress = self.get_progress(duration, time)
            if current_progress > self.progress:
                self.bar.update(current_progress - self.progress)
                self.progress = current_progress

        # display log is true then it will print if errors
        elif display_log:
            print(log)

    @staticmethod
    def get_progress(duration, time):
        """ Returns the progress as percentage from duration and time """
        duration_in_sec = duration.get_time_in_sec()
        if duration_in_sec == 0:
            return 100

        return int(time.get_time_in_sec() * 100 / duration_in_sec)

    def clear(self):
        """ Clears the progress bar """
        self.bar.clear()

    def __del__(self):
        self.bar.close()
        del self.bar
        del self.parser
