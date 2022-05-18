import schedule
import time


class FolderSentinel:
    """a"""

    def __init__(self, folder_path):
        """a"""
        self.folder_path = folder_path

    def start(self):
        """a"""
        print('Folder sentinal has started')
        schedule.every(10).seconds.do(
            self.__check_folder_changes)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def __check_folder_changes(self):
        """a"""
        print('Checking folder changes')
