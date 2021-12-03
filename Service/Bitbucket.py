#!/usr/bin/env python3
import requests
import json
import Service.config

class Bitbucket():
    def __init__(self):
        self.accessToken = ''
        return

    def __connect(self):
        req = requests.post('https://bitbucket.org/site/oauth2/access_token',data={
        	'client_id': Service.config.BITBUCKET_CLIENT_ID,
        	'client_secret': Service.config.BITBUCKET_CLIENT_SECRET,
        	'grant_type': 'client_credentials'
        })
        self.accessToken = json.loads(req.content.decode('utf-8'))['access_token']


    def collectFiles(self):
        self.__connect()
        req = requests.get('https://api.bitbucket.org/2.0/repositories/experius/mage2-module-experius-patcher/src/master/patches?pagelen=100', headers={'Authorization': 'Bearer ' + self.accessToken})
        composer_packs = json.loads(req.content.decode('utf-8'))
        patches = composer_packs['values']
        patchLinks = []

        while 'next' in composer_packs:
            req = requests.get(composer_packs['next'], headers={'Authorization': 'Bearer ' + self.accessToken})
            composer_packs = json.loads(req.content.decode('utf-8'))
            patches = patches + composer_packs['values']

        for patch in patches:
            patchLinks.append(patch['links']['self']['href'])

        return {'experius': patchLinks}