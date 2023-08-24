# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user
from hangman import bcrypt
from hangman.forms.profile_form import ProfileForm
from hangman.forms.change_password_form import ChangePasswordForm
from hangman.photo.save_photo import save_photo
from hangman import db, app
from hangman.hangman_db.models.user import User
from hangman import logger
from typing import Union

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile() -> Union[str, redirect]:
    form = ProfileForm(current_user)
    if form.validate_on_submit():
        if form.photo.data:
            photo = save_photo(form.photo.data)
            current_user.photo = photo
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        logger.info("Your account has been updated!")
        flash("Your account has been updated!", "success")
        return redirect(url_for("profile"))
    else:
        form.username.data = current_user.username
        form.email.data = current_user.email
        photo = url_for("static", filename="profile_photos/" + current_user.photo)
        return render_template(
            "profile.html",
            title="Account",
            form=form,
            photo=photo,
            adminas=current_user.admin if current_user.admin else False,
        )


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password() -> Union[str, redirect]:
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form.old_password.data):
            crypted_password = bcrypt.generate_password_hash(
                form.new_password.data
            ).decode("utf-8")
            user = db.session.get(User, current_user.id)
            user.password = crypted_password
            db.session.add(user)
            db.session.commit()
            logout_user()
            logger.info("Password changed successfully, you can log in again")
            flash("Password changed successfully, you can log in again", "info")
            return redirect(url_for("index"))
        else:
            logger.warning("Invalid current password")
            flash("Invalid current password", "danger")
    return render_template(
        "change_password.html",
        title="Change password",
        form=form,
        adminas=current_user.admin if current_user.admin else False,
    )
