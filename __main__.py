from datetime import datetime, timedelta
from time import sleep
import pathlib
import threading
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileModifiedEvent

PRACTICE_PROBLEMS_FILENAME = "practice_problems.py"


class TestRunner:
    __handler_func = None

    @staticmethod
    def run_tests():
        subprocess.run(["pytest", PRACTICE_PROBLEMS_FILENAME])

    @staticmethod
    def handle_file_modified(event):

        if TestRunner.__handler_func != None:
            TestRunner.__handler_func.cancel()

        TestRunner.__handler_func = threading.Timer(1.0, TestRunner.run_tests)
        TestRunner.__handler_func.start()


if __name__ == "__main__":

    TestRunner.run_tests()

    # Absolute path of current directory.
    current_directory_path = pathlib.Path(__file__).parent.absolute()

    # Absolute path of practice_problems.py in current directory.
    practice_problems_filepath = str(pathlib.PurePath(
        current_directory_path, PRACTICE_PROBLEMS_FILENAME))

    # Class to watch for all types of file change events.
    file_watcher = Observer()

    # Configure handler for specifically for the "file modified event".
    file_modified_event_handler = FileModifiedEvent(practice_problems_filepath)
    #  method to be executed when event fires:
    file_modified_event_handler.dispatch = TestRunner.handle_file_modified

    # Attach the handler to the file watcher.
    file_watcher.schedule(file_modified_event_handler,
                          practice_problems_filepath)
    file_watcher.start()

    print("Watching: " + PRACTICE_PROBLEMS_FILENAME)

    try:
        while file_watcher.is_alive():
            file_watcher.join(1)
    except KeyboardInterrupt:
        file_watcher.stop()

    file_watcher.join()
