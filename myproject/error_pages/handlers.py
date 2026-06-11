from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html') , 404

@error_pages.app_errorhandler(500)
def error_500(error):
    return render_template('error_pages/500.html') , 500

# Test routes to preview error pages
@error_pages.route('/test_404')
def test_404():
    return render_template('error_pages/404.html')

@error_pages.route('/test_500')
def test_500():
    return render_template('error_pages/500.html')
