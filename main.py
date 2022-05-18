from csv import excel
from folder_sentinel import FolderSentinel
from folder_manager import FolderManager
import os

folder_manager = FolderManager(r"C:\Users\ale_a\Desktop\Test")

folder_manager.create_directory("Processed")
folder_manager.create_directory("Not applicable")

if folder_manager.are_there_new_files():
    excel_files = folder_manager.get_excel_files()
    if excel_files is not None:
        print("nice")
    else:
        print("noooo")
else:
    print("No new files to check.")
