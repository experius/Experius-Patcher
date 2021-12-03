#!/usr/bin/env python3
import requests
import json
import Service.config

class Github():
    def __init__(self):
        self.accessToken = ''
        return

    def __connect(self):
        self.accessToken = Service.config.GITHUB_ACCESS_TOKEN

    def collectFiles(self):
        self.__connect()
        req = requests.get('https://api.github.com/repos/magento/quality-patches/contents/patches/', headers={'Authorization': 'Token ' + self.accessToken })
        patchDirs = json.loads(req.content.decode('utf-8'))
        patchFolders = {}
        for patchDir in patchDirs:
            patchLinks = []
            subUrl = patchDir['_links']['self']
            req = requests.get(subUrl)
            patches = json.loads(req.content.decode('utf-8'))
            for patch in patches:
                patchLink = patch['download_url']

                if patchLink.endswith('.patch'):
                    patchLinks.append(patchLink)
            patchFolders[patchDir['name']] = patchLinks

        return patchFolders