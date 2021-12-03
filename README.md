# Experius Patches
The experius patches website provides a collection of commands to collect and download all Magento 2 patches released by both Adobe and Experius.

Patches are collected from the following repositories:
 - https://bitbucket.org/experius/mage2-module-experius-patcher
 - https://github.com/magento/quality-patches

## How to install
Make sure you have a valid version of python 3 installed.

1. Run: ```pip install -r requirements.txt```
2. Create a valid Oauth Key/Value pair on Bitbucket: https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/
3. Create a valid access token on Github: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
4. Create a config.py file in the Service folder based on config.py.sample. Fill in the credentials created in the previous steps.
3. Run: ```bash run.sh```

To collect patch files, run one of the following commands:

 - Experius Patches: ```python3 GetExperiusPatches.py```
 - Adobe Patches: ```python3 GetMagentoPatches.py```
