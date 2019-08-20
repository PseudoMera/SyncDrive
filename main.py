import os
import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


files_extensions = ('.jpg', '.png', '.PNG')
'''
def get_file_last_modified_date(file_name, file_path):
    try:
        decoded_file_path = os.fsdecode(file_path)
        modification_time = os.path.getmtime(f'{decoded_file_path}/{file_name}')
    except OSError:
        modification_time = 0
    return modification_time
    '''


'''Solve problem with date, the script is uploading files that should not be e.g. 19 august - 19 febreuary = 0 so it uploads'''
def file_modification_day(file_name, file_path):
    decoded_file_path = os.fsdecode(file_path)
    modification_time = os.path.getmtime(f'{decoded_file_path}/{file_name}')
    mod_date = repr(datetime.datetime.fromtimestamp(modification_time))
    return int(mod_date[27:29])

def get_all_files(files_path):
    '''login_gdrive()'''
    directory = os.fsencode(files_path)
    for files in os.listdir(directory):
        filename = os.fsdecode(files)
        tmpDir = os.fsdecode(directory)
        if filename.endswith(files_extensions) and abs(file_modification_day(filename, tmpDir) - int(datetime.datetime.today().strftime('%d'))) <= 5:
            drive_file_handler(f'{tmpDir}/{filename}')

'''
def login_gdrive():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
'''
def drive_file_handler(file_path):
    folder_id = '1LypqyXyvfa9kwGptCI0PJoLk15ziOgBo'
    file_drive = drive.CreateFile({"title":file_path[21:],"parents":[{"kind":"drive#fileLink", "id": folder_id}]})
    file_drive.SetContentFile(file_path)
    file_drive.Upload()

if __name__ == "__main__":
    files_path = '/home/albin/Pictures'
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    get_all_files(files_path)
