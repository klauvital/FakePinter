from fakepinter import database, app
from fakepinter.models import Usuario, Foto


with app.app_context():
    database.create_all()