from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return '404 Page Not Found', 404

@error_pages.app_errorhandler(500)
def error_500(error):
    return '500 Internal Server Error', 500
