# pylint: disable-all
from PIL import Image
import os
import secrets
from hangman import app


def save_photo(form_picture):
    random_hex = secrets.token_hex(8)
    _, jpg_or_png = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + jpg_or_png
    picture_path = os.path.join(app.root_path, "static/profile_photos", picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn