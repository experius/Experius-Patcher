import subprocess
import os
import shutil
from utils.CheckAndCreateDir import check_and_create_dir

cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd + '/repositories/shopware-patches')
pull = subprocess.Popen(
    ['git', 'pull', 'origin', 'master']
)
pull.wait()
os.chdir(cwd)

patchesDir = cwd + '/repositories/shopware-patches/patches'
check_and_create_dir(cwd, 'patches/shopware')

for patch in os.listdir(patchesDir):
    fullName = os.path.join(patchesDir, patch)
    if os.path.isfile(fullName) and fullName.endswith('.patch'):
        shutil.copy(fullName, cwd + '/patches/shopware')
