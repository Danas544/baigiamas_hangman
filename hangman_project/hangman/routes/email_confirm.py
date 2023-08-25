# pylint: disable-all
from flask import redirect, url_for, flash
from hangman.hangman_db.models.user import User
from hangman import db, app


@app.route('/confirm/<string:token>')
def confirm_email(token:str) -> redirect:
    try:
        user = User.verify_reset_token(token)
        if user is None:
            flash("The confirmation link is invalid or has expired.", "danger")
            return redirect(url_for("index"))

        if user.email_confirm:
            flash('Account already confirmed. Please login.', 'success')
        else:
            user.email_confirm = True
            db.session.commit()
            flash('You have confirmed your account. Thanks!', 'success')

    except Exception:
        flash('The confirmation link is invalid or has expired.', 'danger')

    return redirect(url_for('login'))
