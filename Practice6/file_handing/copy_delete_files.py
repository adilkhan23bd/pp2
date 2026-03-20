import shutil
import os

source_file = "example.txt"
copy_file = "copy_example.txt"

shutil.copy(source_file, copy_file)
print("File copied successfully")

backup_file = "backup_example.txt"
shutil.copy(source_file, backup_file)
print("Backup created")

file_to_delete = "copy_example.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted")
else:
    print("File not found")