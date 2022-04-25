# Experius Patches
The experius patches website provides a collection of commands to collect and download all Magento 2 and Magento Cloud patches released by both Adobe and Experius.

Patches are collected from the following repositories:
 - https://bitbucket.org/experius/mage2-module-experius-patcher
 - https://github.com/magento/quality-patches
 - https://github.com/magento/magento-cloud-patches

## How to install
Make sure you have a valid version of python 3 installed.

1. Run: ```pip3 install -r requirements.txt```
4. Create a config.py file in the etc folder based on Config.py.sample. Fill in your base_url according to the used url.
3. Run: ```bash run.sh```

To collect patch files, run one of the following commands:

 - Experius Patches: ```python3 GetExperiusPatches.py```
 - Magento Quality Patches: ```python3 GetMagentoPatches.py```
 - Magento Cloud Patches: ```python3 GetCloudPatches.py```
