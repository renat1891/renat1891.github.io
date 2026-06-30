from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, session

# 1. Захист головної сторінки адмінки (/admin/)
class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        # Якщо в сесії є позначка, що користувач увійшов — пускаємо
        return session.get('logged_in') == True
    def inaccessible_callback(self, name, **kwargs):
        # Якщо ні — перенаправляємо на нашу сторінку входу
        return redirect(url_for('login'))
    

# 2. Захист сторінок керування моделями (наприклад, керування користувачами)
class SecureModelView(ModelView):
    def is_accessible(self):
        return session.get('logged_in') == True
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))