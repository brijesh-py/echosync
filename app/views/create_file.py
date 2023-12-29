from app import app
import os
from app.views.utils import Utils

class FileEditor:
    def open_file(self, file_name, file_content):
        filename = Utils().check_file_exists(file_name)
        file_path = os.path.join(app.config["UPLOAD_FILES"], filename)
        try:
            with open(file_path, 'w') as file:
                file.write(str(file_content))
                file.close()
            file.filename= filename
            file.content_type = str(os.path.splitext(file_path)[1])[1:]
            Utils().utils(file=file, create_file=True)
            return True
        except Exception as e:
            # Log the error or print it for debugging
            return False
        
            