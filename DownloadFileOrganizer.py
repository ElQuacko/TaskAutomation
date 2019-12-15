import shutil, os

text_files = [".txt"]
grapic_files = [".jpg", ".bmp", ".png", ".gif", ".psd"]
office_files = [".doc", ".xlsx", ".ppt", ".ods"]
pdf_files = [".pdf"]
other_files = [".mobi", ".exe"]
zip_files = [".zip"]
music_files = [".mp3"]
video_files = [".mp4"]

text_folder = (r"D:\WWW\github\TaskAutomation\Text folder")
graphic_folder = (r"D:\WWW\github\TaskAutomation\Graphic folder")
office_folder = (r"D:\WWW\github\TaskAutomation\Office folder")
pdf_folder = (r"D:\WWW\github\TaskAutomation\PDF folder")
other_folder = (r"D:\WWW\github\TaskAutomation\Other folder")
zip_folder = (r"D:\WWW\github\TaskAutomation\ZIP folder")
music_folder = (r"D:\WWW\github\TaskAutomation\Music folder")
video_folder = (r"D:\WWW\github\TaskAutomation\Video folder")

file_extensions = [text_files, grapic_files, office_files, pdf_files, other_files, zip_files, music_files, video_files]
folders = [text_folder, graphic_folder, office_folder, pdf_folder, other_folder, zip_folder, music_folder, video_folder]

source = (r"D:\WWW\github\TaskAutomation")

def fileTransporter(file_type, file_folder, destination_folder):
    file_folder_list = os.listdir(file_folder)

    for files in file_folder_list:
        try:
            if os.path.isfile(files) and files.endswith(file_type):
                shutil.move(files, destination_folder)
        except:
            print("ERROR: Something went wrong")

for extension, folder in zip(file_extensions, folders):
    for file_type in range(len(extension)):
        print(extension[file_type])
        fileTransporter(extension[file_type], source, folder)
