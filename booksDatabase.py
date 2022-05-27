from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class BooksPredictions(db.Model):
    id = db.Column('book_id', db.Integer, primary_key = True)
    Genre = db.Column(db.String(100))
    Confidence = db.Column(db.String(100))  
    FileName = db.Column(db.String(100))


    def __init__(self, Genre, Confidence, FileName):
        self.Genre = Genre
        self.Confidence = Confidence
        self.FileName = FileName
