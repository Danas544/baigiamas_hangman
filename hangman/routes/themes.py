# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from hangman import db, app
from hangman.forms.new_theme_form import ThemeForm
from hangman.hangman_db.models.theme import Theme



def get_available_themes(db_session):
    themes = db_session.query(Theme).filter_by(activate=1).all()
    return themes


@app.route("/themes", methods=["GET", "POST"])
@login_required
def themes():
    if current_user.admin:
        all_themes = Theme.query.all()
        return render_template(
            "themes.html",
            title="Themes",
            all_themes=all_themes,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))



@app.route("/new_theme", methods=["GET", "POST"])
@login_required
def new_theme():
    if current_user.admin:
        forma = ThemeForm()
        if forma.validate_on_submit():
            new_theme = Theme(
                name=forma.name.data,
                activate=forma.activate.data,
            )
            db.session.add(new_theme)
            db.session.commit()
            flash(f"New theme successfully created", "success")
            return redirect(url_for("themes"))
        return render_template(
            "add_theme.html",
            form=forma,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))



@app.route("/theme/delete/<int:id>")
@login_required
def delete(id):
    if current_user.admin:
        theme = Theme.query.get(id)
        db.session.delete(theme)
        db.session.commit()
        return redirect(url_for("themes"))
    else:
        return redirect(url_for("index"))



@app.route("/theme/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    if current_user.admin:
        forma = ThemeForm()
        theme = Theme.query.get(id)
        if forma.validate_on_submit():
            theme.name = forma.name.data
            theme.activate = forma.activate.data
            db.session.commit()
            db.session.refresh(theme)
            return redirect(url_for("themes"))
        print(theme.activate)
        return render_template(
            "update_theme.html",
            form=forma,
            theme=theme,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))

