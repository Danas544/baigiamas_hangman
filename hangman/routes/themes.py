# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from hangman import db, app
from hangman.forms.new_theme_form import ThemeForm
from typing import List, Union
from sqlalchemy.orm import Session
from hangman.hangman_db.models.theme import Theme
from hangman.hangman_db.models.word import Word
from hangman import logger

def get_available_themes(db_session: Session) -> List[Theme]:
    themes = db_session.query(Theme).filter_by(activate=1).all()
    return themes


@app.route("/themes", methods=["GET", "POST"])
@login_required
def themes() -> Union[str, redirect]:
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
def new_theme() -> Union[str, redirect]:
    if current_user.admin:
        forma = ThemeForm()
        if forma.validate_on_submit():
            new_theme = Theme(
                name=forma.name.data,
                activate=forma.activate.data,
            )
            db.session.add(new_theme)
            db.session.commit()
            logger.info("New theme successfully created")
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
def delete(id: int) -> redirect:
    if current_user.admin:
        theme = Theme.query.get(id)
        db.session.delete(theme)
        words = Word.query.filter_by(theme_id=id).all()
        for word in words:
            db.session.delete(word)
        db.session.commit()
        logger.info("Theme successfully deleted")
        flash(f"Theme successfully deleted", "success")
        return redirect(url_for("themes"))
    else:
        return redirect(url_for("index"))


@app.route("/theme/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id:int) -> Union[str, redirect]:
    if current_user.admin:
        theme = Theme.query.get(id)
        forma = ThemeForm(theme)
        if forma.validate_on_submit():
            theme.name = forma.name.data
            theme.activate = forma.activate.data
            db.session.commit()
            db.session.refresh(theme)
            logger.info("Theme successfully updated")
            flash(f"Theme successfully updated", "success")
            return redirect(url_for("themes"))
        return render_template(
            "update_theme.html",
            form=forma,
            theme=theme,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))
