from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

@app.route('/')
def home():
    
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
        names.append(name)
        return redirect(url_for('form'))
    
    return render_template('form.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)