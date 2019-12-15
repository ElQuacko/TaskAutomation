import shutil, os

file_extensions = ".txt"
source = (r"D:\WWW\github\TaskAutomation")
destination = (r"D:\WWW\github\TaskAutomation\Txt test")

def fileTransporter(file_type, file_folder, destination_folder):
    file_folder_list = os.listdir(file_folder)

    for files in file_folder_list:
        try:
            if os.path.isfile(files) and files.endswith(file_type):
                shutil.move(files, destination_folder)
        except:
            print("ERROR: Something went wrong")

fileTransporter(file_extensions, source, destination)
