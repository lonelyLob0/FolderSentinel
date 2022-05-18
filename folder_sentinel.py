from scheduler import Scheduler
import datetime as date_time

class FolderSentinel:
    """a"""

    def __init__(self, folder_path):
        """a"""
        self.folder_path = folder_path
        self.schedule = Scheduler()

    def start(self):
        """a"""
        print('Folder sentinal has started')
        self.schedule.minutely(date_time.time(second=3),
                               self.__check_folder_changes())

    def __check_folder_changes(self):
        """a"""
        print('Checking folder changes')
