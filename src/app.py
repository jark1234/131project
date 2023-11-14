from flask import Flask, render_template, request, redirect, url_for

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


if __name__ == '__main__':
    app.run(debug=True)
