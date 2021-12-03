from Cron.GetPatches import GetPatches
from Service.Github import Github

class Magento(GetPatches):
    def __init__(self):
        super().__init__()
        self.service = Github()