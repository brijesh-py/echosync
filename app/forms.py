from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators, StringField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileRequired, FileAllowed, FileField, FileSize

class FileUploadForm(FlaskForm):
    file_input = FileField('File', validators=[FileRequired(), FileSize(max_size=100 * 1024 * 1024, message='File size must be less than 10MB')])

class CustomFile(FlaskForm):
    custom_filename =  StringField('File name', validators=[DataRequired(Length(max=20, min=8))])
    custom_file_content = TextAreaField("File content", validators=[DataRequired(Length(max=5000, min=10))])
