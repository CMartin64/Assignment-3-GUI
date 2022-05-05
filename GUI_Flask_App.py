from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
print('got here')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = './'

bookDetails = {}
bookDetails['Title'] = 'Mr Smithsonian'
bookDetails['Author'] = 'Mrs Smithsonian'
bookDetails['Genre'] = 'Biographical'
bookDetails['Publisher'] = 'Self-Published'

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite3'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'the random string'    
db = SQLAlchemy(app)

class Books(db.Model):
   id = db.Column('book_id', db.Integer, primary_key = True)
   Title = db.Column(db.String(100))
   Author = db.Column(db.String(100))  
   Genre = db.Column(db.String(100))
   Publisher = db.Column(db.String(10))
   
   def __init__(self, Title, Author, Genre,Publisher):
    self.Title = Title
    self.Author = Author
    self.Genre = Genre
    self.Publisher = Publisher

db.create_all()

entry = Books('Life of Student', 'Callum Freeburn', 'Fiction', 'self-publisher')
db.session.add(entry)
db.session.commit()

users = Books.query.all()

# for user in users:
#     print(user.Title)

def allowed_file(filename):     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))


@app.route('/bookDetails')
def book_details():
    return render_template('book_details.html', bookDetails=bookDetails, image = 'static/pic_trulli.jpg')

@app.route('/show_all')
def show_all():
   return render_template('show_all.html', Books = Books.query.all() )

if __name__ == '__main__':
    app.run(debug=True)
