import subprocess
import os
import shutil

pull = subprocess.Popen(['git', 'pull', 'origin' , 'master'], cwd=os.path.dirname(os.path.realpath(__file__)) + '/repositories/quality-patches')
pull.wait()

mainDir = os.path.dirname(os.path.realpath(__file__)) + '/repositories/quality-patches/patches'

if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/patches'):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/patches')

subDirs = os.listdir(mainDir)
for subDir in subDirs:
    subPath= os.path.join(mainDir, subDir)

    if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/patches/' + subDir):
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/patches/' + subDir)

    for patch in os.listdir(subPath):
        fullName = os.path.join(subPath, patch)
        if os.path.isfile(fullName) and fullName.endswith('.patch'):
            shutil.copy(fullName, os.path.dirname(os.path.realpath(__file__)) + '/patches/' + subDir)