import json
from flask.json import jsonify
from flask import render_template
from werkzeug.exceptions import RequestURITooLarge
from Models.Compatibility import Compatibility
import os
from etc import Config

class ComposerUpload():
    def __init__(self) -> None:
        self.compatibility = None

    def nl2br(self, s):
        return '<br />\n'.join(s.split('\n'))

    def execute(self, composerlock):
        lockContents = composerlock.stream.read()
        lock = json.loads(lockContents)
        modules = lock['packages']
        self.compatibility = Compatibility(modules)

        result = {
            'extra': {
                'composer-exit-on-patch-failure': True,
                'patches': {}
            }
        }

        basePatchPath = os.getcwd() + "/patches/experius"
        patches = os.listdir(basePatchPath)
        patches.sort()
        for patch in patches:
            if self.compatibility.isCompatible(patch): 
                patchNum = self.compatibility.getPatchNum(patch)
                url = Config.BASE_URL + "patches/experius/" + patch
                result['extra']['patches'][patchNum] = url
        
        responseData = {
            'title': 'Composer Check',
            'back': '/',
            'base_url': Config.BASE_URL,
            'result': json.dumps(result, indent=4)
        }

        return render_template('checkcomposer.html', data = responseData)