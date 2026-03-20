import shutil
import os

base_path = r"C:\Users\Адильхан\Desktop\pp2\work\Practice6"

source = os.path.join(base_path, "example.txt")
destination_dir = os.path.join(base_path, "test_dir")
destination = os.path.join(destination_dir, "example.txt")


os.makedirs(destination_dir, exist_ok=True)


shutil.move(source, destination)
print("File moved successfully")