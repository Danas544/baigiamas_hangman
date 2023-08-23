# pylint: disable-all
from flask import render_template
from flask_login import current_user, login_required
from hangman import app
from hangman.hangman_db.crud import get_user_stats


@app.route("/user_stats", methods=["GET"])
@login_required
def user_stats() -> str:
    stats = get_user_stats(current_user)
    total_score = sum(stats.score for stats in stats)
    total_win = sum(1 for stats in stats if stats.type == "win")
    total_lose = sum(1 for stats in stats if stats.type == "lose")
    return render_template(
        "user_stats.html",
        title="User stats",
        user_stats=stats,
        total_score=total_score,
        total_win=total_win,
        total_lose=total_lose,
        adminas=current_user.admin if current_user.admin else False,
    )
