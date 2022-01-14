from flask import Flask, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from Controllers.ComposerUpload import ComposerUpload
from Controllers.Patches import Patches
from Controllers.Homepage import Homepage
from Controllers.CheckComposer import CheckComposer
from Controllers.ComposerUpload import ComposerUpload
from Controllers.ApiPatchesList import ApiPatchesList

app = Flask(__name__)

@app.route("/")
def homePage():
    homePageController = Homepage()
    return homePageController.execute()

@app.route("/patches/")
@app.route("/patches")
def getFolders():
    patchesController = Patches()
    return patchesController.execute(None, None)

@app.route("/patches/<subfolder>/")
@app.route("/patches/<subfolder>")
def getPatchList(subfolder):
    patchesController = Patches()
    return patchesController.execute(subfolder, None)

@app.route("/patches/<subfolder>/<patch>/")
@app.route("/patches/<subfolder>/<patch>")
def getPatch(subfolder, patch):
    patchesController = Patches()
    return patchesController.execute(subfolder, patch)

@app.route("/check/composer/")
@app.route("/check/composer")
def checkComposer():
    checkComposerController = CheckComposer()
    return checkComposerController.execute()

@app.route("/check/composer/", methods=['POST'])
@app.route("/check/composer", methods=['POST'])
def uploadComposer():
    composerUpload = ComposerUpload()
    composerlock = request.files['composerlock']
    if composerlock.filename == '':
        return redirect(url_for('checkComposer'))

    return composerUpload.execute(composerlock)

@app.route("/api/patches/list/")
def apiPatchesList():
    apiPatchesList = ApiPatchesList()
    return apiPatchesList.execute()

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
