from cryptography.fernet import Fernet
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    encrypted_password = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, title, content, password):
        self.title = title
        self.content = content
        self.encrypted_password, self.key = encrypt_password(password)

    def decrypt_password(self):
        cipher_suite = Fernet(self.key)
        return cipher_suite.decrypt(self.encrypted_password).decode()

def encrypt_password(password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode()), key

