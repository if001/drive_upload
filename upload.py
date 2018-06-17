from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import glob
import sys
UPLOAD_FILE_DIR = '/home/i_fujimoto/word_features/char_autoencoder/preprocessing'
EXTENSION = 'npz'
FOLDER_ID = "1MNg_alSewFxSC0VSgYFaAwRpJgdoi4D-"
FOLDER_ID = "1obg3fGOa-UyEoAB_GLiSUbm2jZ1432pX"
def upload_file_list():
    file_path = os.path.join(UPLOAD_FILE_DIR, '*.' + EXTENSION)
    files = glob.glob(file_path)
    if not files:
        print("not files to upload")
        sys.exit(0)
    return files
def drive_auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive
def file_upload(drive, file_name):
    title = file_name.split("/")[-1]
    u_file = drive.CreateFile({
        'title': title,
        'parents': [{'kind': 'drive#fileLink', 'id':FOLDER_ID}]
    })
    u_file.SetContentFile(file_name)
    try:
        print("upload " + title)
        u_file.Upload()
    except:
        print(file_name + " upload faild")


def main():
    files = upload_file_list()
    drive = drive_auth()

    for f in files:
        file_upload(drive, f)

if __name__ == "__main__":
    main()
