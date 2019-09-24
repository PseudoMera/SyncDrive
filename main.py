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


def file_modification_day(file_name, file_path):
    decoded_file_path = os.fsdecode(file_path)
    modification_time = os.path.getmtime(f'{decoded_file_path}/{file_name}')
    mod_date = repr(datetime.datetime.fromtimestamp(modification_time))
    temp = ''
    for ch in mod_date:
        if ch != ',':
            temp  = f'{temp}{ch}'
    return int(str.strip(temp[25:27]))

def file_modification_month(file_name, file_path):
    decoded_file_path = os.fsdecode(file_path)
    modification_time = os.path.getmtime(f'{decoded_file_path}/{file_name}')
    mod_date = repr(datetime.datetime.fromtimestamp(modification_time))
    temp = ''
    for ch in mod_date:
        if ch != ',':
            temp  = f'{temp}{ch}'
    return int(str.strip(temp[23:25]))

def get_all_files(files_path):
    directory = os.fsencode(files_path)
    for files in os.listdir(directory):
        filename = os.fsdecode(files)
        tmpDir = os.fsdecode(directory)
        if filename.endswith(files_extensions) and abs(file_modification_day(filename, tmpDir) - int(datetime.datetime.today().strftime('%d'))) <= 5 and abs(file_modification_month(filename, tmpDir) - int(datetime.datetime.today().strftime('%m'))) == 0:
            drive_file_handler(f'{tmpDir}/{filename}')


def drive_file_handler(file_path):
    folder_id = 'Your folder id'
    file_drive = drive.CreateFile({"title":file_path[21:],"parents":[{"kind":"drive#fileLink", "id": folder_id}]})
    file_drive.SetContentFile(file_path)
    file_drive.Upload()

if __name__ == "__main__":
    files_path = '/home/albin/Pictures'
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    get_all_files(files_path)
