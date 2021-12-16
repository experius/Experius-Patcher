import requests
import os

class GetPatches():
    def __init__(self):
        self.service = None
        self.patches = []

    def getPatches(self):
        self.patches = self.service.collectFiles()
        patchesDir = os.path.dirname(os.path.realpath(__file__)) + '/../patches'

        if not os.path.exists(patchesDir):
            os.makedirs(patchesDir)

        for patchFolder in self.patches:
            patches = self.patches[patchFolder]
            subDir = patchesDir + '/' + patchFolder

            if not os.path.exists(subDir):
                os.makedirs(subDir)
            
            for patch in patches:
                req = requests.get(patch)
                if req.status_code == 200:
                    patchFileData = req.content.decode('utf-8')

                    file = os.open(subDir + '/' + patch.rsplit('/', 1)[-1], os.O_RDWR|os.O_CREAT)
                    os.write(file, patchFileData.encode())
                    os.close(file)