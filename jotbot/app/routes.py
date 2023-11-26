import json
from flask import Flask, render_template, request, redirect, url_for
from app import myapp_obj, db

app = Flask(__name__)
app.secret_key = 'testkey'  

users = {'novel': 'alam'}  


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
             return redirect(url_for('welcome'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/create.note', methods=['POST'])
def create_note():
    note_text = request.form['note_text']
    notes.append({'text': note_text})
    save_notes()
    return index()

@app.route('/delete_note/<int: note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    if request.method == 'POST':
        #deletes note
        del notes[note_id]
        save_notes()
    #return updated index page
    return index()

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

if __name__ == '__main__':
    app.run(debug=True)
