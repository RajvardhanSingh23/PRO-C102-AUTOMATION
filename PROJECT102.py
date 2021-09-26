import cv2,dropbox,time,random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.A5Py5fvKtcJaEUesfD7fy9XZkxsX0eJy54se-bdBCKR5K_PSCasvoBucxsezZVEtdiMytsItPiWJy9Y4iEaUg4ydhrla9N87sgAEUgHOxdGoKXckW9ZZ27IV9jnnpHOA_CLpoFE"
    file = img_name
    file_from = file
    file_to="/class102/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()