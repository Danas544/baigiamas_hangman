# pylint: disable-all
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user
from hangman import bcrypt
from hangman.forms.profile_form import ProfileForm
from hangman.forms.change_password_form import ChangePasswordForm
from hangman.photo.save_photo import save_photo
from hangman import db, app
from hangman.hangman_db.models.user import User
from hangman.hangman_db.crud import get_all_stats


@app.route("/all_stats", methods=["GET"])
@login_required
def all_stats():
    all_stats = get_all_stats()

    user_total_scores = {}
    user_total_wins = {}
    user_total_losses = {}
    user_names = {}
    user_photos = {}

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
    print(sorted_users)
    return render_template(
        "all_user_stats.html",
        title="User stats",
        user_stats=all_stats,
        user_total_scores=user_total_scores,
        user_total_wins=user_total_wins,
        user_total_losses=user_total_losses,
        user_names=user_names,
        user_photos=user_photos,
        sorted_users=sorted_users,
        adminas=current_user.admin if current_user.admin else False,
    )
