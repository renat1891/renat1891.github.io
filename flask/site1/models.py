from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<User {self.username} ({self.age})>'
    
    def __str__(self):
        return f'{self.username} ({self.age})'