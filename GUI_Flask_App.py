from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

print('got here')
# def create_app():


bookDetails = {}
bookDetails['Title'] = 'Mr Smithsonian'
bookDetails['Author'] = 'Mrs Smithsonian'
bookDetails['Genre'] = 'Biographical'


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite3'
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))


@app.route('/bookDetails')
def book_details():
    return render_template('book_details.html', bookDetails=bookDetails, image = 'static/pic_trulli.jpg')

@app.route('/show_all')
def show_all():
   return render_template('show_all.html', Books = Books.query.all() )

if __name__ == '__main__':
    app.run(debug=True)
