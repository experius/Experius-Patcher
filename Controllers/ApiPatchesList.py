import os
from flask import jsonify
from etc import Config

class ApiPatchesList():
    
    def execute(self):
        allPatches = {}

        basePatchPath = os.getcwd() + "/patches/experius"
        patches = os.listdir(basePatchPath)

        for patch in patches:
            allPatches[patch.split('_')[0]] = Config.BASE_URL + "patches/experius/" + patch

        return jsonify(allPatches)