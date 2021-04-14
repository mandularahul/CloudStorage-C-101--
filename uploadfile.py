import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Asx8A6Em7Ex-zxQpBt8rdbogLSaEISyLzVvG4XQCfplJqTUVWfniTeEK8gWp5koBZCTETt_I0Vxdzz8RYnCAFiPPQj4J2J1Vp3S5PQnqcrCOhLzpNXif2keew31kp9XyjLQ6jgg'
    transferData = TransferData(access_token)

    file_from = input(r'Enter file path')  #r'C:\Users\Mitanshu\Downloads\pdf\Charts.pdf'
    file_to =  '/test_dropbox/2.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()