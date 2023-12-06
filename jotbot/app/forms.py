from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo

# English Forms #

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

# Home Page Form
class HomePageForm(FlaskForm):
    homePage = SubmitField('Home')

# Signup Form
class SignupForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create Account')

# Logout Form
class LogoutForm(FlaskForm):
    submitLogout = SubmitField('Logout')

# Create Note Form
class CreateNoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Create Note')

# Edit Note Form
class EditNoteForm(FlaskForm):
    note_id = HiddenField('Note ID')
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Save Changes')

# Delete Note Form
class DeleteNoteForm(FlaskForm):
    note_id = HiddenField('Note ID')
    submit = SubmitField('Delete')

# Delete Account Form
class DeleteAccountForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Delete Account')

# Spanish Forms #

# Login Form (Spanish)
class SLoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Clave', validators=[DataRequired()])
    remember_me = BooleanField('Acuérdate de mí')
    submit = SubmitField('Iniciar sesión')

# Home Page Form (Spanish)
class SHomePageForm(FlaskForm):
    homePage = SubmitField('Inicio')

# Signup Form (Spanish)
class SSignupForm(FlaskForm):
    email = StringField('Dirección de correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password', message='Las contraseñas deben coincidir')])
    submit = SubmitField('Crear cuenta')

# Logout Form (Spanish)
class SLogoutForm(FlaskForm):
    submitLogout = SubmitField('Cerrar sesión')

# Create Note Form (Spanish)
class SCreateNoteForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    text = TextAreaField('Texto', validators=[DataRequired()])
    submit = SubmitField('Crear nota')

# Edit Note Form (Spanish)
class SEditNoteForm(FlaskForm):
    note_id = HiddenField('ID de la nota')
    title = StringField('Título', validators=[DataRequired()])
    text = TextAreaField('Texto', validators=[DataRequired()])
    password = PasswordField('Contraseña')
    submit = SubmitField('Guardar cambios')

# Delete Note Form (Spanish)
class SDeleteNoteForm(FlaskForm):
    note_id = HiddenField('ID de la nota')
    submit = SubmitField('Eliminar')

# Delete Account Form (Spanish)
class SDeleteAccountForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Eliminar cuenta')
