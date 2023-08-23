# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from hangman import db, app
from hangman.hangman_db.models.word import Word
from hangman.forms.new_word_form import WordForm
from hangman import logger
from typing import Union

@app.route("/themes/<string:name>/<int:theme_id>/words", methods=["GET", "POST"])
@login_required
def word(name:str, theme_id:int) -> Union[str, redirect]:
    if current_user.admin:
        all_words_by_theme = Word.query.filter_by(theme_id=theme_id).all()
        return render_template(
            "words.html",
            title=f"Words by theme {name}",
            all_words_by_theme=all_words_by_theme,
            theme_name=name,
            theme_id=theme_id,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))


@app.route("/themes/<string:name>/<int:theme_id>/new_word", methods=["GET", "POST"])
@login_required
def new_word(name:str, theme_id:int) -> Union[str, redirect]:
    if current_user.admin:
        forma = WordForm(theme_id)
        if forma.validate_on_submit():
            new_word = Word(
                name=forma.name.data, activate=forma.activate.data, theme_id=theme_id
            )
            db.session.add(new_word)
            db.session.commit()
            logger.info("New word successfully created")
            flash(f"New word successfully created", "success")
            return redirect(url_for("word", name=name, theme_id=theme_id))
        return render_template(
            "add_word.html",
            form=forma,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))


@app.route("/themes/<string:theme_name>/<int:theme_id>/word/delete/<int:word_id>")
@login_required
def delete_word(theme_name:str, theme_id:int, word_id:int) -> redirect:
    if current_user.admin:
        word = Word.query.get(word_id)
        db.session.delete(word)
        db.session.commit()
        logger.info("Word successfully deleted")
        flash(f"Word successfully deleted", "success")
        return redirect(url_for("word", name=theme_name, theme_id=theme_id))
    else:
        return redirect(url_for("index"))


@app.route(
    "/themes/<string:theme_name>/<int:theme_id>/word/update/<int:word_id>", methods=["GET", "POST"]
)
@login_required
def update_word(theme_name:str, theme_id:int, word_id:int) -> Union[str, redirect]:
    if current_user.admin:
        word = Word.query.get(word_id)
        forma = WordForm(theme_id,word)
        if forma.validate_on_submit():
            word.name = forma.name.data
            word.activate = forma.activate.data
            db.session.commit()
            logger.info("Word successfully updated")
            flash(f"Word successfully updated", "success")
            return redirect(url_for("word", name=theme_name, theme_id=theme_id))
        return render_template(
            "update_word.html",
            form=forma,
            word=word,
            adminas=current_user.admin if current_user.admin else False,
        )
    else:
        return redirect(url_for("index"))
