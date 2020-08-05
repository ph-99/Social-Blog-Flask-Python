# HANDLERS.PY

from flask import render_template , request , Blueprint,url_for

error_pages = Blueprint('error_pages' , __name__)

# we connect it to a general handler
@error_pages.app_errorhandler(404)
def error_404(error):
    # tuple
    return render_template('error_pages/404.html') , 404

#forbidden access
@error_pages.app_errorhandler(403)
def error_403(error):
    # tuple
    return render_template('error_pages/403.html') , 404
