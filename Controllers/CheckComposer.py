from flask import render_template
from etc import Config

class CheckComposer():
    def execute(self):
        return render_template('checkcomposer.html', data = {
            'title': 'Composer Check',
            'base_url': Config.BASE_URL,
            'back': '/'
        })
