from flask import render_template
from etc import Config

class Homepage():
    def execute(self):
        return render_template('linklist.html', data = {
            'base_url': Config.BASE_URL,
            'title': 'Experius Patches',
            'path': '',
            'links': {
                'patches'
            }
        })
