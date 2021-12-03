from Cron.GetPatches import GetPatches
from Service.Bitbucket import Bitbucket

class Experius(GetPatches):
    def __init__(self):
        super().__init__()
        self.service = Bitbucket()