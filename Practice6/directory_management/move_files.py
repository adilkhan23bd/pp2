import shutil
import os


source = "example.txt"
destination = "test_dir/example.txt"


os.makedirs("test_dir", exist_ok=True)

shutil.move(source, destination)
print("File moved successfully")