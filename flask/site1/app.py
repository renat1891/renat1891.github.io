# pip install Flask-SQLAlchemy
# pip install Flask-Admin


from flask import Flask, render_template, redirect, url_for, request, session

from database import db
from models import User
from admin_view import SecureAdminIndexView, SecureModelView, Admin


app = Flask(__name__)
app.secret_key = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Економія пам'яті, відключаємо відстеження змін у базі даних


db.init_app(app)

with app.app_context():
    db.create_all()


admin = Admin(
    app, 
    name='Панель Керування', 
    index_view=SecureAdminIndexView()
)

admin.add_view(SecureModelView(User, db.session))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        
        # Проста перевірка пароля (можна змінити на будь-який інший)
        if password == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('admin.index')) # Редірект в адмінку
        else:
            error = 'Неправильний пароль!'
            
    return render_template('admin/login.html', error=error)


# Маршрут для виходу
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


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