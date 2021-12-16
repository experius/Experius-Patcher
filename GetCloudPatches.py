import subprocess
import os
import shutil

pull = subprocess.Popen(['git', 'pull', 'origin' , 'develop'], cwd=os.path.dirname(os.path.realpath(__file__)) + '/repositories/magento-cloud-patches')
pull.wait()

mainDir = os.path.dirname(os.path.realpath(__file__)) + '/repositories/magento-cloud-patches/patches'

if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/patches'):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/patches')
if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) + '/patches/cloud'):
    os.makedirs(os.path.dirname(os.path.realpath(__file__)) + '/patches/cloud')

for patch in os.listdir(mainDir):
    fullName = os.path.join(mainDir, patch)
    if os.path.isfile(fullName) and fullName.endswith('.patch'):
        shutil.copy(fullName, os.path.dirname(os.path.realpath(__file__)) + '/patches/cloud')