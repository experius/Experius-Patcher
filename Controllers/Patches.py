from flask import send_file, abort, render_template
import os
from etc import Config

class Patches():

    def execute(self, subfolder, patch):
        if not patch:
            if not subfolder:
                filePath = os.getcwd() + '/patches'
                if not os.path.exists(filePath):
                    abort(404)
                
                subDirs = os.listdir(filePath)
                subDirs.sort()

                return render_template('linklist.html', data = {
                    'title': 'Patches',
                    'back': '/',
                    'base_url': Config.BASE_URL,
                    'path': 'patches/', 
                    'links': subDirs
                })

            filePath = os.getcwd() + '/patches/' + subfolder
            if not os.path.exists(filePath):
                abort(404)
                
            patches = os.listdir(filePath)
            patches.sort()

            links = []

            for ptch in patches:
                links.append({
                    'name': ptch
                })

            return render_template('patchlist.html', data = {
                'title': subfolder.title(),
                'back': 'patches/',
                'base_url': Config.BASE_URL,
                'path': 'patches/' + subfolder + '/',
                'patches': links
            })

        file = os.getcwd() + '/patches/' + subfolder + '/' + patch

        if os.path.isfile(file):
            return send_file(file, mimetype='text/plain')
            
        abort(404)
