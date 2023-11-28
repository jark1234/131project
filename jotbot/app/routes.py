import json
from flask import Flask, render_template, request, redirect, url_for, flash
from . import myapp_obj, db
from app.models import Note, User
from app.forms import LoginForm, HomePageForm, SignupForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


users = {'novel': 'alam'}  


@myapp_obj.route('/')
def home():
    return redirect(url_for('login'))


@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    current_form = LoginForm()
    errorMessage = ''

    if current_form.validate_on_submit():
        email = current_form.email.data
        user = User.query.filter_by(email=email).first()
        
        if user:
            # Debug output
            print(f"Entered Email: {email}")
            print(f"Retrieved User: {user.email}") 
            print(f"Stored Password Hash: {user.password}")

        if user and check_password_hash(user.password, current_form.password.data):
            print(f"Entered Password: {current_form.password.data}")
            print("Password Matched!")
            login_user(user, remember=current_form.remember_me.data)
            return redirect('/welcome')

    return render_template('login.html', current_form=current_form, error=errorMessage)

@myapp_obj.route('/welcome')
def welcome():
    return render_template('welcome.html')

@myapp_obj.route('/create_account', methods=['GET', 'POST'])
def create_account():
    current_form = SignupForm()
    errorMessage = ''

    if current_form.validate_on_submit():   
        email = current_form.email.data
        password = current_form.password.data
        confirm_password = current_form.confirm_password.data

        if password != confirm_password:
            error = 'Passwords do not match'
            return render_template('create_account.html', error=error)
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            errorMessage = 'Email already exists, please log in'
            return render_template('create_account.html', form=current_form, error=errorMessage)
        
        user = User(email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. Please log in.')
        return redirect(url_for('login'))        #redirect to login page when implemented
    else:
        print("Form failed")
        print(current_form.errors)

    return render_template('create_account.html',form=current_form, error = errorMessage)

@myapp_obj.route('/create.note', methods=['POST'])
def create_note():
    note_text = request.form['note_text']
    new_note = Note(text=note_text)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('welcome'))

@myapp_obj.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('welcome'))

def load_notes():
    global notes 
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent = 4)


