from csv import excel
from folder_sentinel import FolderSentinel
from folder_manager import FolderManager
from excel_manager import ExcelManager

folder_manager = FolderManager(r"C:\Users\ale_a\Desktop\Test")

processed_folder_path = folder_manager.create_directory("Processed")
not_applicable_folder_path = folder_manager.create_directory("Not applicable")

origin_file = r"C:\Users\ale_a\Desktop\Test\file_to_consolidate.xlsx"
target_file = r"C:\Users\ale_a\Desktop\Test\Master\master.xlsx"

em = ExcelManager()
em.create_master_workflow(r"C:\Users\ale_a\Desktop\Test")

em.consolidate_excel_file_in_target(origin_file, target_file)

FolderManager.move_files_to_directory(origin_file,directory_path=processed_folder_path)

# if folder_manager.are_there_new_files():
# excel_files = folder_manager.get_excel_files()
# if excel_files is not None:
# print("nice")
# else:
# print("noooo")
# else:
#print("No new files to check.")
