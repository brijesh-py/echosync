from app import app
import os
from app.views.utils import Utils

class FileEditor:
    def open_file(self, file_name, file_content):
        file_path = os.path.join(app.config["UPLOAD_FILES"], file_name)
        try:
            with open(file_path, 'w') as file:
                file.write(str(file_content))
                file.close()
                file.filename = file_name
                file.content_type = str(os.path.splitext(file_path)[1])[1:]
                update_file_path = os.path.join(app.config["UPLOAD_FILES"], file_name)
            Utils().upload_file_data(file, update_file_path)
            return True
        except Exception as e:
            # Log the error or print it for debugging
            return False
        
            