import schedule
import time
from folder_manager import FolderManager
from excel_manager import ExcelManager


class FolderSentinel:
    """a"""

    def __init__(self, folder_path,period_in_seconds):
        """a"""
        #General variables
        self.__period_in_seconds = period_in_seconds

        # Folder management related variables.
        self.folder_path = folder_path
        self.processed_folder_path = ""
        self.not_applicable_folder_path = ""

        self.__fm = FolderManager(self.folder_path)

        # Excel variables.
        self.__em = ExcelManager()

    def __create_folder_structure(self):
        """a"""
        self.processed_folder_path = self.__fm.create_directory("Processed")
        self.not_applicable_folder_path = self.__fm.create_directory(
            "Not applicable")

    def __create_excel_master_workflow(self):
        """a"""
        self.__em.create_master_workflow(self.folder_path)

    def start(self):
        """a"""
        print('Folder sentinal has started...')
        print('Folder structure has been created...')
        self.__create_folder_structure()
        self.__create_excel_master_workflow()

        self.__check_folder_changes()

        schedule.every(self.__period_in_seconds).seconds.do(
            self.__check_folder_changes)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def __check_folder_changes(self):
        """a"""
        print('Checking folder changes')

        if self.__fm.are_there_new_files():
            print('New files were found, checking them...')
            excel_files = self.__fm.get_excel_files()
            if excel_files is not None:
                print('Checking excel files...')
                for file in excel_files:
                    self.__em.consolidate_excel_file_in_target(
                        file, self.__em.get_master_path)
                self.__fm.move_files_to_directory(
                    excel_files, directory_path=self.processed_folder_path)
                
            print('Checking other files...')
            other_files = self.__fm.get_all_files()
            self.__fm.move_files_to_directory(
                other_files, directory_path=self.not_applicable_folder_path)

        else:
            print("No new files were found...")
