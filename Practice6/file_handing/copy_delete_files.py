import shutil
import os

base_path = r"C:\Users\Адильхан\Desktop\pp2\work\Practice6"

source_file = os.path.join(base_path, "example.txt")
copy_file = os.path.join(base_path, "copy_example.txt")
backup_file = os.path.join(base_path, "backup_example.txt")


shutil.copy(source_file, copy_file)
print("File copied successfully")


shutil.copy(source_file, backup_file)
print("Backup created")


if os.path.exists(copy_file):
    os.remove(copy_file)
    print("File deleted")
else:
    print("File not found")