from app import db

class FilesDB(db.Model):
    def __init__(self, file_name, upload_time, file_size, file_type, file_key, file_icon):
        self.file_name = file_name
        self.upload_time = upload_time 
        self.file_size = file_size 
        self.file_type = file_type 
        self.file_key = file_key
        self.file_icon = file_icon
    
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    upload_time = db.Column(db.String(30), nullable=False)
    file_size = db.Column(db.String(30), nullable=False)
    file_type = db.Column(db.String(40), nullable=False)
    file_key = db.Column(db.String(30), nullable=False, unique=True)
    file_icon = db.Column(db.String())

    def __repre__(self):
        return f"<File {self.file_name} >"
    
