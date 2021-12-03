import requests
import os

class GetPatches():
    def __init__(self):
        self.service = None
        self.patches = []

    def getPatches(self):
        self.patches = self.service.collectFiles()
        for patch in self.patches:
            print(patch)
            req = requests.get(patch)
            if req.status_code == 200:
                patchFileData = req.content.decode('utf-8')
                
                if not os.path.exists(os.getcwd() + '/patches'):
                    os.makedirs(os.getcwd() + '/patches')

                file = os.open(os.getcwd() + '/patches/' + patch.rsplit('/', 1)[-1], os.O_RDWR|os.O_CREAT)
                os.write(file, patchFileData.encode())
                os.close(file)