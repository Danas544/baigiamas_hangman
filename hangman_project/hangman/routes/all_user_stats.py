# pylint: disable-all
from flask import render_template, url_for
from flask_login import current_user, login_required
from hangman import app
from hangman.hangman_db.crud import get_all_stats
from typing import Dict, List, Tuple, Union

@app.route("/all_stats", methods=["GET"])
@login_required
def all_stats() -> str:
    all_stats = get_all_stats()

    user_total_scores: Dict[int, int] = {}
    user_total_wins: Dict[int, int] = {}
    user_total_losses: Dict[int, int] = {}
    user_names: Dict[int, str] = {}
    user_photos: Dict[int, str] = {}

    for stats in all_stats:
        user_id = stats.user_id
        username = stats.user.username
        photo = url_for("static", filename="profile_photos/" + stats.user.photo)

        if user_id not in user_total_scores:
            user_total_scores[user_id] = 0
            user_total_wins[user_id] = 0
            user_total_losses[user_id] = 0
            user_names[user_id] = username
            user_photos[user_id] = photo

        user_total_scores[user_id] += stats.score
        if stats.type == "win":
            user_total_wins[user_id] += 1
        elif stats.type == "lose":
            user_total_losses[user_id] += 1

    sorted_users = [
        (rank + 1, user_id)
        for rank, user_id in enumerate(
            sorted(
                user_total_scores.keys(),
                key=lambda x: user_total_scores[x],
                reverse=True,
            )
        )
    ]
    return render_template(
        "all_user_stats.html",
        title="User stats",
        user_stats=all_stats,
        user_total_scores=user_total_scores,
        user_total_wins=user_total_wins,
        user_total_losses=user_total_losses,
        user_names=user_names,
        user_photos=user_photos,
        sorted_users=sorted_users
    )
