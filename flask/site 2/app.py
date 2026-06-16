from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reviews = [
            {"name": "Олексій", "text": "Чудовий сервіс!", "rating": 5},
            {"name": "Марія", "text": "Непогано, але можна краще.", "rating": 4}
        ]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        rating = int(request.form['rating'])

        reviews.append({"name": name, "text": text, "rating": rating})

        # return redirect(url_for('index'))
    
    return render_template('index.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)