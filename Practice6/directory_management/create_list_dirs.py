import os


os.mkdir("test_dir")
print("Directory 'test_dir' created")
 

os.makedirs("parent/child/grandchild", exist_ok=True)
print("Nested directories created")


current_dir = os.getcwd()
print("Current directory:", current_dir)


items = os.listdir()
print("Files and directories:", items)


folders = [item for item in items if os.path.isdir(item)]
print("Folders:", folders)


files = [item for item in items if os.path.isfile(item)]
print("Files:", files)