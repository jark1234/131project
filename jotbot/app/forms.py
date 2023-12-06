from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class HomePageForm(FlaskForm):
    homePage = SubmitField('Home')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create Account')

class LogoutForm(FlaskForm):
    submitLogout = SubmitField('Logout')

class CreateNoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Create Note')

class EditNoteForm(FlaskForm):
    note_id = HiddenField('Note ID')
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Save Changes')

class DeleteNoteForm(FlaskForm):
    note_id = HiddenField('Note ID')
    submit = SubmitField('Delete')

class DeleteAccountForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Delete Account')

class ProfileForm(FlaskForm):
    submit = SubmitField('Profile')
    
class ProfileEditForm(FlaskForm):
    dob = StringField('yyy-mm-dd', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Save') 
