import os
import shutil

SOURCE_FOLDER = r"E:\coding\TestFolder"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js"]
}
for folder in FILE_TYPES.keys():
    os.makedirs(os.path.join(SOURCE_FOLDER, folder), exist_ok=True)

os.makedirs(os.path.join(SOURCE_FOLDER, "Others"), exist_ok=True)
for file in os.listdir(SOURCE_FOLDER):

    file_path = os.path.join(SOURCE_FOLDER, file)
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()
        moved = False
        for folder, extensions in FILE_TYPES.items():

            if extension in extensions:

                shutil.move(
                    file_path,
                    os.path.join(SOURCE_FOLDER, folder, file)
                )

                print(f"Moved: {file} -> {folder}")
                moved = True
                break
        if not moved:
            shutil.move(
                file_path,
                os.path.join(SOURCE_FOLDER, "Others", file)
            )
            print(f"Moved: {file} -> Others")

print("\nFile organization completed successfully!")