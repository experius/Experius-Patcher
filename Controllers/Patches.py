from flask import send_file, abort
import os

class Patches():
    def execute(self, patch):
        file = os.getcwd() + '/patches/' + str(patch)

        if os.path.isfile(file):
            return send_file(file, mimetype='text/plain')

        abort(404)
