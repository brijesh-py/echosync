from flask import render_template, redirect, request, json, jsonify, flash, url_for
from app.forms import FileUploadForm, CustomFile
from app import app
from app.views.create_file import FileEditor
from app.config import compare_time
from app.models import FilesDB
from app.views.utils import Utils
import os


class App:
    @app.template_global()
    def formate_datetime(date):
        return compare_time(str(date))

    def home_page(self):
        file_upload_form = FileUploadForm()
        custom_file = CustomFile()
        files = FilesDB.query.order_by(FilesDB.upload_time.desc()).limit(20).all()
        return render_template(
            "index.html",
            form=file_upload_form,
            custom_file=custom_file,
            files=files,
            compare_time=compare_time,
        )

    def create_custom_file(self):
        custom_file = CustomFile()
        if request.method == "POST" and custom_file.validate_on_submit():
            file_name = custom_file.custom_filename.data
            file_content = custom_file.custom_file_content.data
            response = FileEditor().open_file(
                file_name=file_name, file_content=file_content
            )
            if response:
                flash("Successfully created file!", ["bg__success", ""])
            else:
                flash("File not created?", ["bg__error", str(custom_file.errors)])
            return redirect(url_for("app.home_page"))
        else:
            return redirect(url_for("app.home_page"))

    def save_file(self, file):
        file_path = os.path.join(app.config["UPLOAD_FILES"], file.filename)
        file.save(file_path)
        Utils().upload_file_data(file, file_path)

    def upload_files_page(self):
        file_upload_form = FileUploadForm()
        if (
            request.method == "POST"
            and file_upload_form.validate_on_submit()
            and file_upload_form.file_input.data
        ):
            file_data = request.files["file_input"]
            self.save_file(file_data)
            flash("Successfully uploaded file!", ["bg__success", ""])
        else:
            flash("File not uploaded?", ["bg__error", str(file_upload_form.errors)])
        return redirect(url_for("app.home_page"))
