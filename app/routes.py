from flask import Blueprint
from app.views.views import App

app_bp = Blueprint('app', __name__)

# routes
app_bp.add_url_rule("/", view_func=App().home_page, methods=['GET'])
app_bp.add_url_rule("/upload-file/", view_func=App().upload_files_page, methods=['POST', 'GET'])
app_bp.add_url_rule("/custom-file/",view_func=App().create_custom_file, methods=['GET','POST'])

