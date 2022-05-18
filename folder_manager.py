from pathlib import Path
import os
import shutil


class FolderManager:
    """a"""

    def __init__(self, folder_path):
        """a"""
        self.folder_path = Path(folder_path)

    @staticmethod
    def directory_exists(directory_path):
        """a"""
        return os.path.isdir(directory_path)

    def create_directory(self, directory_name):
        """a"""
        new_folder = self.folder_path / directory_name
        if not __class__.directory_exists(new_folder):
            os.mkdir(new_folder)
        return new_folder

    def are_there_new_files(self):
        """a"""
        paths = [p for p in self.folder_path.iterdir() if p.is_file()]
        return len(paths) > 0

    def get_excel_files(self):
        """a"""
        files = [p for p in self.folder_path.glob("*.xlsx")]
        return files if len(files) > 0 else None

    def get_all_files(self):
        """a"""
        files = [p for p in self.folder_path.glob("*.*")]
        return files if len(files) > 0 else None

    @staticmethod
    def move_files_to_directory(*files, directory_path):
        """a"""

        for file in files[0]:
            shutil.move(file, directory_path)
