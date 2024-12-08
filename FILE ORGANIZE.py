
import os
import pathlib
import shutil

#creating directories of file
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
     "XML": [".xml"],
   "EXE": [".exe"],
   "SHELL": [".sh"]
   
}

#creating of list of directory and file formats
format_types = list(DIRECTORIES.keys())
file_format = list(DIRECTORIES.values())

print(file_format)
print(format_types)

# Create folders for each directory type if they do not exist
for folder in format_types:
    if not os.path.isdir(folder):
        print(f"Creating folder: {folder}")
        os.mkdir(folder)

# Add an "others" folder for unidentified file types
if not os.path.isdir("others"):
    print("Creating 'others' folder")
    os.mkdir("others")


for file in os.scandir():
    if file.is_file():
        file_name = pathlib.Path(file)

# Get the file type (extension)
        file_type = file_name.suffix.lower()  

        dest = "others" 

        
#giving index of file in sequence
        for folder, extensions in DIRECTORIES.items():
            if file_type in extensions:
                dest = folder
            

        # Move the file to the valid folder
        src = str(file_name)
        
        if dest != "others":
            print(f"Moving {src} to {dest} folder.")
        else:
            print(f"{src} cannot identify file type.")

      
        if not os.path.isdir(dest):
            os.mkdir(dest)
        shutil.move(src, os.path.join(dest, file_name.name))

 #procedure

print("File organization completed.")
input("\nPress Enter to exit.")