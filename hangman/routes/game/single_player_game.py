from flask import render_template, request, session, flash, redirect, url_for
from flask_login import current_user, login_required
from hangman import app
from hangman.game_logic.hangman_game import HangmanGame
from hangman.hangman_db.crud import insert_stats


@app.route("/single-player-game/<theme_id>", methods=["GET", "POST"])
@login_required
def single_player_game(theme_id):
    end_game = False
    if f"hangman_game_{current_user.id}" not in session or session[
        f"hangman_game_{current_user.id}"
    ]["theme_id"] != int(theme_id):
        hangman_game = HangmanGame()
        try:
            hangman_game.select_theme(int(theme_id))
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for("theme_selection"))
        except TypeError as e:
            flash("Select theme", "danger")
            return redirect(url_for("theme_selection"))
        hangman_game.start_single_player_game()
        session[f"hangman_game_{current_user.id}"] = hangman_game.get_game_data()
    else:
        hangman_game_data = session[f"hangman_game_{current_user.id}"]
        hangman_game = HangmanGame.from_dict(hangman_game_data)

    if request.method == "POST" and "letter" in request.form:
        letter = request.form["letter"]
        game_output = hangman_game.guess_letter(letter)
        if hangman_game.is_game_over():
            insert_stats(
                current_user=current_user,
                type="win" if hangman_game.win is True else "lose",
                score=hangman_game.get_guesses_left(),
            )
            session.pop(f"hangman_game_{current_user.id}")
            end_game = True
    else:
        game_output = ""

    if end_game is False:
        session[f"hangman_game_{current_user.id}"] = hangman_game.get_game_data()
    
    return render_template(
        "single_player_game.html",
        hangman_game=hangman_game,
        game_output=game_output,
        theme_id=theme_id,
        end_game=end_game,
        user_photo=current_user.photo
    )
