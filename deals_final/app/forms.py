from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename




class LoginForm(FlaskForm):
	file = FileField(validators=[FileRequired()])
	member = IntegerField('member', validators=[DataRequired()])
	submit = SubmitField('Sign In')
