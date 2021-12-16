import subprocess
import os
import shutil

pull = subprocess.Popen(['git', 'pull', 'origin' , 'master'], cwd=os.path.dirname(os.path.realpath(__file__)) + '/repositories/mage2-module-experius-patcher')
pull.wait()

patchesDir = os.path.dirname(os.path.realpath(__file__)) + '/repositories/mage2-module-experius-patcher/patches'

if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/patches'):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/patches')
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/patches/experius'):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/patches/experius')

for patch in os.listdir(patchesDir):
    fullName = os.path.join(patchesDir, patch)
    if os.path.isfile(fullName) and fullName.endswith('.patch'):
        shutil.copy(fullName, os.path.dirname(os.path.realpath(__file__)) + '/patches/experius')