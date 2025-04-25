import os
import shutil
os.makedirs("New_Subdirectory", exist_ok=True)
shutil.copy("source_file.txt", "New_Subdirectory/destination_file.txt")
print("File copied successfully.")
