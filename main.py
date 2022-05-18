from folder_sentinel import FolderSentinel

watched_folder = r"C:\Users\ale_a\Desktop\Test"

sentinel = FolderSentinel(watched_folder,period_in_seconds=20)

sentinel.start()
