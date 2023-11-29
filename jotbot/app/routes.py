import json
from flask import Flask, render_template, request, redirect, url_for, flash
from . import myapp_obj, db
from app.models import Note, User
from app.forms import LoginForm, HomePageForm, SignupForm, CreateNoteForm, DeleteNoteForm, EditNoteForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

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
            return redirect('/create_note')

    return render_template('login.html', current_form=current_form, error=errorMessage)

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

@myapp_obj.route('/create_note', methods=['GET', 'POST'])
@login_required
def create_note():
    current_form = CreateNoteForm()

    # Check for the edited_note_id query parameter
    if 'message' in request.args:
        message_category = request.args['message_category']
        flash(request.args['message'], message_category)

    if current_form.validate_on_submit():
            # Create a new note
        note_title = current_form.title.data
        note_text = current_form.text.data

        if note_title.strip() and note_text.strip():
            new_note = Note(title=note_title, data=note_text, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
        
        flash('Note successfully added', 'success')  # Add this line to display a flash message

    user_notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date.desc()).all()
    return render_template('create_note.html', current_form=current_form, user_notes=user_notes)


@myapp_obj.route('/delete_note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    current_form = DeleteNoteForm()
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('create_note'))

@myapp_obj.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    edit_form = EditNoteForm()
    note = Note.query.get_or_404(note_id)

    if edit_form.validate_on_submit():
        print(f"Form Text Data: {edit_form.text.data}")

        note.title = edit_form.title.data
        note.data = edit_form.text.data
        note.date = datetime.utcnow()
        db.session.commit()

        flash('Note successfully edited', 'success')
        return redirect(url_for('create_note', edited_note_id=note.id))
    else:
        # Populate the form with existing note data
        edit_form.note_id.data = note.id
        edit_form.title.data = note.title
        edit_form.text.data = note.data

    
    return render_template('edit_note.html', edit_form=edit_form, note=note)




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


