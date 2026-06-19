# pip install Flask-SQLAlchemy


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Економія пам'яті, відключаємо відстеження змін у базі даних

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def __str__(self):
        return self.username

with app.app_context():
    db.create_all()
    

@app.route('/')
def home():
    names = User.query.all()
    
    return render_template('index.html', names=names)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
def user(username):
    return f'Hello, {username}!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'This is post number {post_id}.'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['myname']
        db.session.add(User(username=name))
        db.session.commit()
        return redirect(url_for('form'))
    
    names = User.query.all()
    return render_template('form.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)