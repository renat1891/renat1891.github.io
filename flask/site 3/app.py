from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "gallery-secret-2024"

photos = [
    {"id": 1,  "title": "Ранок над Дніпром",   "author": "Тарас Коваль",   "category": "Пейзаж",      "year": 2023, "location": "Київ, Україна",     "desc": "Перші промені сонця крізь туман.",          "img": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=900&q=80"},
    {"id": 2,  "title": "Старе місто",          "author": "Оксана Мельник", "category": "Архітектура", "year": 2022, "location": "Львів, Україна",    "desc": "Брукована вулиця середмістя.",               "img": "https://images.unsplash.com/photo-1467803738586-46b7eb7b16a1?w=900&q=80"},
    {"id": 3,  "title": "Погляд",               "author": "Іван Петренко",  "category": "Портрет",     "year": 2024, "location": "Одеса, Україна",    "desc": "Вуличний портрет у золоту годину.",          "img": "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=900&q=80"},
    {"id": 4,  "title": "Карпатський ліс",      "author": "Тарас Коваль",   "category": "Природа",     "year": 2023, "location": "Закарпаття",        "desc": "Ранковий туман між смереками.",               "img": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=900&q=80"},
    {"id": 5,  "title": "Базарний день",        "author": "Оксана Мельник", "category": "Вулиця",      "year": 2022, "location": "Чернівці, Україна", "desc": "Сцена з центрального ринку.",                "img": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=900&q=80"},
    {"id": 6,  "title": "Блакитна година",      "author": "Іван Петренко",  "category": "Пейзаж",      "year": 2024, "location": "Херсон, Україна",   "desc": "Захід на березі річки.",                     "img": "https://images.unsplash.com/photo-1504701954957-2010ec3bcec1?w=900&q=80"},
    {"id": 7,  "title": "Відображення",         "author": "Тарас Коваль",   "category": "Абстракція",  "year": 2023, "location": "Харків, Україна",   "desc": "Геометрія скла і неба.",                     "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&q=80"},
    {"id": 8,  "title": "Зимовий ліхтар",      "author": "Оксана Мельник", "category": "Вулиця",      "year": 2021, "location": "Полтава, Україна",  "desc": "Перший сніг у вечірньому місті.",            "img": "https://images.unsplash.com/photo-1491314169072-84ae3ab3c80b?w=900&q=80"},
    {"id": 9,  "title": "Дитинство",            "author": "Іван Петренко",  "category": "Портрет",     "year": 2024, "location": "Вінниця, Україна",  "desc": "Безтурботна мить гри.",                      "img": "https://images.unsplash.com/photo-1565793979386-845e4a7e2a1f?w=900&q=80"},
    {"id": 10, "title": "Бузок після дощу",     "author": "Тарас Коваль",   "category": "Природа",     "year": 2022, "location": "Умань, Україна",    "desc": "Квіти у краплях весняного дощу.",            "img": "https://images.unsplash.com/photo-1582738411706-bfc8e691d1c2?w=900&q=80"},
    {"id": 11, "title": "Залізниця",            "author": "Оксана Мельник", "category": "Архітектура", "year": 2023, "location": "Дніпро, Україна",   "desc": "Металевий ритм залізничного моста.",         "img": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=900&q=80"},
    {"id": 12, "title": "Осіннє золото",        "author": "Іван Петренко",  "category": "Пейзаж",      "year": 2024, "location": "Буковель, Україна", "desc": "Ліс у жовтні — мов картина.",                "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&q=80"},
]

_next_id = len(photos) + 1


def get_categories():
    return sorted({p["category"] for p in photos})



@app.route("/")
def home():
    featured = photos[:6]
    stats = {
        "total":      len(photos),
        "categories": len(get_categories()),
        "authors":    len({p["author"] for p in photos}),
    }
    return render_template("home.html", featured=featured, stats=stats, active="home")


@app.route("/gallery")
def gallery():
    category = request.args.get("category", "all")
    q        = request.args.get("q", "").strip().lower()

    filtered = photos
    if category != "all":
        filtered = [p for p in filtered if p["category"] == category]
    if q:
        filtered = [p for p in filtered if
                    q in p["title"].lower() or
                    q in p["author"].lower() or
                    q in p["location"].lower()]

    return render_template(
        "gallery.html",
        photos=filtered,
        total=len(photos),
        categories=get_categories(),
        active_category=category,
        q=q,
        active="gallery",
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    global _next_id

    if request.method == "POST":
        title    = request.form.get("title", "").strip()
        author   = request.form.get("author", "").strip()
        category = request.form.get("category", "").strip()
        year     = request.form.get("year", "").strip()
        location = request.form.get("location", "").strip()
        desc     = request.form.get("desc", "").strip()
        img_url  = request.form.get("img_url", "").strip()

        errors = []
        if not title:
            errors.append("Назва обов'язкова.")
        if not author:
            errors.append("Автор обов'язковий.")

        if errors:
            return render_template("add.html", errors=errors,
                                   categories=get_categories(), active="add",
                                   form=request.form)

        photos.insert(0, {
            "id":       _next_id,
            "title":    title,
            "author":   author,
            "category": category or "Без категорії",
            "year":     int(year) if year.isdigit() else 2024,
            "location": location or "Невідоме місце",
            "desc":     desc,
            "img":      img_url or "https://images.unsplash.com/photo-1519974719765-e6559eac2575?w=900&q=80",
        })
        _next_id += 1

        flash("Фотографію успішно додано до галереї!", "success")
        return redirect(url_for("gallery"))

    return render_template("add.html", errors=[], categories=get_categories(),
                           active="add", form={})


@app.route("/about")
def about():
    team = [
        {"name": "Оксана Мельник", "role": "Куратор",    "img": "https://i.pravatar.cc/150?img=47"},
        {"name": "Тарас Коваль",   "role": "Фотограф",   "img": "https://i.pravatar.cc/150?img=33"},
        {"name": "Іван Петренко",  "role": "Розробник",  "img": "https://i.pravatar.cc/150?img=12"},
        {"name": "Марія Бондар",   "role": "Дизайнер",   "img": "https://i.pravatar.cc/150?img=5"},
    ]
    stats = {
        "photographers": 247,
        "works":         len(photos),
        "founded":       2019,
    }
    return render_template("about.html", team=team, stats=stats, active="about")



if __name__ == "__main__":
    app.run(debug=True)