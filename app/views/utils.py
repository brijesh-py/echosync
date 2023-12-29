import os
from app.models import FilesDB
from app.config import get_time, key
from app import db


class Utils:
    def get_file_icon(self, file):
        try:
            file_types = {
                "pdf": "pdf.png",
                "jpg": "image.png",
                "jpeg": "image.png",
                "png": "image.png",
                "svg": "image.png",
                "gif": "image.png",
                "txt": "file.png",
                "doc": "document.png",
                "docx": "document.png",
                "xls": "spreadsheet.png",
                "xlsx": "spreadsheet.png",
                "ppt": "presentation.png",
                "pptx": "presentation.png",
                "mp3": "audio.gif",
                "wav": "audio.gif",
                "mp4": "video.png",
                "avi": "video.png",
                "zip": "zip.png",
                "rar": "zip.png",
                "gz": "zip.png",
                "exe": "exe.png",
                "deb": "package.png",
                "rpm": "package.png",
                "py": "python.png",
                "html": "html.png",
                "css": "css.png",
                "db": "db.png",
                "js": "js.png",
                "php": "php.png",
                "deb": "deb.png",
                "img": "img.png",
                "sh": "sh.png",
                "bash": "sh.png",
                "zsh": "sh.png",
                "json": "code.png",
                "xml": "code.png",
                "sql": "db.png",
                "sqlite": "db.png",
                "log": "log.png",
                "xz": "tar.png",
                "gz": "tar.png",
                "md": "readme.png",
                "gitignore": "git.png",
                "application": "mobile-application.png",
            }
            return file_types[file]
        except:
            return "file.png"

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
        file_extension = os.path.splitext(file.filename)[1][1:].lower()
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
