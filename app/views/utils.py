import os
from app.models import FilesDB
from app.config import get_time, key
from app import db


class Utils:
    def get_file_icon(self, file):
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension == ".pdf":
            return "pdf.png"
        if "image" in file:
            return "image.png"
        if "application" in file:
            return "mobile-application.png"
        if "text" in file:
            return "file.png"
        if "video" in file:
            return "video.png"
        else:
            return "document.png"

    def get_file_size(self, file):
        bytes_size = os.path.getsize(file)
        kb_size = bytes_size / 1024
        mb_size = kb_size / 1024

        if mb_size >= 1:
            return f"{mb_size:.2f} MB"
        if kb_size >= 1:
            return f"{kb_size:.2f} KB"
        return f"{bytes_size} Bytes"

    def upload_file_data(self, file, file_path):
        file_extension = os.path.splitext(file.filename)[1].lower()
        file_icon = self.get_file_icon(file_extension)

        file_db = FilesDB(
            file_name=file.filename,
            upload_time=get_time(),
            file_size=self.get_file_size(file_path),
            file_type=file.content_type,
            file_key=key(),
            file_icon=file_icon,
        )
        db.session.add(file_db)
        db.session.commit()
