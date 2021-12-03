from flask import Flask, abort
from Controllers.Patches import Patches

app = Flask(__name__)

@app.route("/patches/<subfolder>/<patch>")
def getPatch(subfolder, patch):
    patchesController = Patches()
    return patchesController.execute(subfolder, patch)

@app.errorhandler(404)
def page_not_found(error):
    return "404 Patch not found", 404

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run()
