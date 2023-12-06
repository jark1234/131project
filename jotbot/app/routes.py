from flask import Flask, render_template, request, redirect, url_for, flash
from . import myapp_obj, db
from app.models import Note, User
from app.forms import LoginForm, HomePageForm, SignupForm, CreateNoteForm, DeleteNoteForm, EditNoteForm, LogoutForm, DeleteAccountForm, ProfileEditForm 
#import spanish forms
from app.forms import SCreateNoteForm, SDeleteAccountForm, SDeleteNoteForm, SEditNoteForm, SHomePageForm, SLoginForm, SLogoutForm, SSignupForm, SProfileEditForm, SProfileForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

import pytz

from datetime import datetime

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

        if user and check_password_hash(user.password, current_form.password.data):
            print("Password Matched!")
            login_user(user, remember=current_form.remember_me.data)
            return redirect('/create_note')
        else:
            errorMessage = 'Invalid email or password. Please try again.'

    return render_template('login.html', current_form=current_form, error=errorMessage)


@myapp_obj.route('/create_account', methods=['GET', 'POST'])
def create_account():
    current_form = SignupForm()
    errorMessage = ''

    if current_form.validate_on_submit():
        username = current_form.username.data   
        email = current_form.email.data
        password = current_form.password.data
        confirm_password = current_form.confirm_password.data

        if password != confirm_password:
            errorMessage = 'Passwords do not match'
            return render_template('create_account.html', error=error)
        elif not(validPassword(password)):
            errorMessage = 'Password must be longer than 8 characters'
            return render_template('create_account.html', form=current_form, error=errorMessage)

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            errorMessage = 'Username is already taken. Please choose another.'
            return render_template('create_account.html', form=current_form, error=errorMessage)        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            errorMessage = 'Email already exists, please log in'
            return render_template('create_account.html', form=current_form, error=errorMessage)
        
        user = User(username = username, email=email, password=generate_password_hash(password))
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

    if current_form.validate_on_submit():
        note_title = current_form.title.data
        note_text = current_form.text.data

        if note_title.strip() and note_text.strip():
            utc_now = datetime.utcnow()
            timezone = pytz.utc
            pdt_timezone = pytz.timezone('America/Los_Angeles')  # Use 'America/Los_Angeles' for PDT
            pdt_now = utc_now.replace(tzinfo=timezone).astimezone(pdt_timezone)

            print("Storing timestamp:", pdt_now)  # Add this line for debugging

            new_note = Note(title=note_title, data=note_text, user_id=current_user.id, date=pdt_now)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('create_note'))
        
        flash('Note successfully added', 'success')  # Add this line to display a flash message

    user_notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date.desc()).all()
    for note in user_notes:
        note.date = note.date.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/Los_Angeles'))
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

    if request.method == 'POST' and edit_form.validate_on_submit():
        note.title = edit_form.title.data
        note.data = edit_form.text.data
        note.date = datetime.utcnow()
        db.session.commit()
        flash('Note successfully edited', 'success')
        return redirect(url_for('create_note'))

    # Populate the form with existing note data
    edit_form.note_id.data = note.id
    edit_form.title.data = note.title
    edit_form.text.data = note.data

    return render_template('edit_note.html', edit_form=edit_form, note=note)

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_form = LogoutForm()
    logout_user()
    return redirect(url_for('login'))    

@myapp_obj.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    delete_account_form = DeleteAccountForm()

    if delete_account_form.validate_on_submit():
        provided_password = delete_account_form.password.data

        # Verify the provided password against the stored hash
        if check_password_hash(current_user.password, provided_password):
            # Delete the user account and redirect to the login page
            db.session.delete(current_user)
            db.session.commit()
            logout_user()
            flash('Account successfully deleted', 'success')
            return redirect(url_for('login'))
        else:
            flash('Incorrect password. Account not deleted.', 'error')

    return render_template('delete_account.html', delete_account_form=delete_account_form)

@myapp_obj.route('/profile' )
@login_required
def profile():
    username = current_user.username
    email = current_user.email
    password = current_user.password
    dob = current_user.dob
    return render_template("profile.html", username = username, email = email, password = password, dob=dob)


@myapp_obj.route('/profile_edit', methods = ['GET', 'POST'])
@login_required
def profile_edit():
    current_form = ProfileEditForm()
    user = User.query.filter_by(username=current_user.username).first() #retreiving current user
    if request.method == 'POST' and current_form.validate_on_submit():
        if current_form.username.data != current_user.username and User.query.filter_by(username=current_form.username.data).first():
            flash('Username is already taken. Please choose another.', 'danger')
            return redirect(url_for('profile_edit'))
        else:
            user.dob = current_form.dob.data            #updating dob of user
            user.username = current_form.username.data
            db.session.commit()
            login_user(User.query.get(user.id))

        return redirect(url_for('profile')) #redirects to profile after submitting form, will show updated dob, username
    return render_template('profile_edit.html', form=current_form)

#helper function

def validPassword(string):
    if len(string) < 8:
        return False
    return True

#spanish version
@myapp_obj.route('/')
def Shome():
    return redirect(url_for('Slogin'))


@myapp_obj.route('/Slogin', methods=['GET', 'POST'])
def Slogin():
    current_form = SLoginForm()
    errorMessage = ''

    if current_form.validate_on_submit():
        email = current_form.email.data
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, current_form.password.data):
            print("Password Matched!")
            login_user(user, remember=current_form.remember_me.data)
            return redirect('/Screate_note')
        else:
            errorMessage = 'Invalid email or password. Please try again.'

    return render_template('Slogin.html', current_form=current_form, error=errorMessage)


@myapp_obj.route('/Screate_account', methods=['GET', 'POST'])
def Screate_account():
    current_form = SSignupForm()
    errorMessage = ''

    if current_form.validate_on_submit():
        username = current_form.username.data   
        email = current_form.email.data
        password = current_form.password.data
        confirm_password = current_form.confirm_password.data

        if password != confirm_password:
            errorMessage = 'Passwords do not match'
            return render_template('create_account.html', error=error)
        elif not(validPassword(password)):
            errorMessage = 'Password must be longer than 8 characters'
            return render_template('Screate_account.html', form=current_form, error=errorMessage)

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            errorMessage = 'Username is already taken. Please choose another.'
            return render_template('Screate_account.html', form=current_form, error=errorMessage)        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            errorMessage = 'Email already exists, please log in'
            return render_template('Screate_account.html', form=current_form, error=errorMessage)
        
        user = User(username = username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully. Please log in.')
        return redirect(url_for('Slogin'))        #redirect to login page when implemented
    else:
        print("Form failed")
        print(current_form.errors)

    return render_template('Screate_account.html',form=current_form, error = errorMessage)

@myapp_obj.route('/Screate_note', methods=['GET', 'POST'])
@login_required
def Screate_note():
    current_form = SCreateNoteForm()

    if current_form.validate_on_submit():
        note_title = current_form.title.data
        note_text = current_form.text.data

        if note_title.strip() and note_text.strip():
            utc_now = datetime.utcnow()
            timezone = pytz.utc
            pdt_timezone = pytz.timezone('America/Los_Angeles')  # Use 'America/Los_Angeles' for PDT
            pdt_now = utc_now.replace(tzinfo=timezone).astimezone(pdt_timezone)

            print("Storing timestamp:", pdt_now)  # Add this line for debugging

            new_note = Note(title=note_title, data=note_text, user_id=current_user.id, date=pdt_now)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('Screate_note'))
        
        flash('Note successfully added', 'success')  # Add this line to display a flash message

    user_notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date.desc()).all()
    for note in user_notes:
        note.date = note.date.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/Los_Angeles'))
    return render_template('Screate_note.html', current_form=current_form, user_notes=user_notes)



@myapp_obj.route('/Sdelete_note/<int:note_id>', methods=['POST'])
@login_required
def Sdelete_note(note_id):
    current_form = SDeleteNoteForm()
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('Screate_note'))

@myapp_obj.route('/Sedit_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def Sedit_note(note_id):
    edit_form = SEditNoteForm()
    note = Note.query.get_or_404(note_id)

    if request.method == 'POST' and edit_form.validate_on_submit():
        note.title = edit_form.title.data
        note.data = edit_form.text.data
        note.date = datetime.utcnow()
        db.session.commit()
        flash('Note successfully edited', 'success')
        return redirect(url_for('Screate_note'))

    # Populate the form with existing note data
    edit_form.note_id.data = note.id
    edit_form.title.data = note.title
    edit_form.text.data = note.data

    return render_template('Sedit_note.html', edit_form=edit_form, note=note)

@myapp_obj.route('/Slogout')
@login_required
def Slogout():
    logout_form = SLogoutForm()
    logout_user()
    return redirect(url_for('Slogin'))    

@myapp_obj.route('/Sdelete_account', methods=['GET', 'POST'])
@login_required
def Sdelete_account():
    delete_account_form = SDeleteAccountForm()

    if delete_account_form.validate_on_submit():
        provided_password = delete_account_form.password.data

        # Verify the provided password against the stored hash
        if check_password_hash(current_user.password, provided_password):
            # Delete the user account and redirect to the login page
            db.session.delete(current_user)
            db.session.commit()
            logout_user()
            flash('Account successfully deleted', 'success')
            return redirect(url_for('Slogin'))
        else:
            flash('Incorrect password. Account not deleted.', 'error')

    return render_template('Sdelete_account.html', delete_account_form=delete_account_form)

@myapp_obj.route('/Sprofile' )
@login_required
def Sprofile():
    username = current_user.username
    email = current_user.email
    password = current_user.password
    dob = current_user.dob
    return render_template("Sprofile.html", username = username, email = email, password = password, dob=dob)


@myapp_obj.route('/Sprofile_edit', methods = ['GET', 'POST'])
@login_required
def Sprofile_edit():
    current_form = SProfileEditForm()
    user = User.query.filter_by(username=current_user.username).first() #retreiving current user
    if request.method == 'POST' and current_form.validate_on_submit():
        if current_form.username.data != current_user.username and User.query.filter_by(username=current_form.username.data).first():
            flash('Username is already taken. Please choose another.', 'danger')
            return redirect(url_for('Sprofile_edit'))
        else:
            user.dob = current_form.dob.data            #updating dob of user
            user.username = current_form.username.data
            db.session.commit()
            login_user(User.query.get(user.id))

        return redirect(url_for('Sprofile')) #redirects to profile after submitting form, will show updated dob, username
    return render_template('Sprofile_edit.html', form=current_form)







