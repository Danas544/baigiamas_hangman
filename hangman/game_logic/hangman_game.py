import random
from typing import Dict, Any, List, Set, Union, Tuple
from hangman.hangman_db.models.theme import Theme
from hangman.hangman_db.models.word import Word
from hangman import db
from hangman import logger

class HangmanGame:
    HANGMAN_DRAWINGS: List[str] = [
        "0.png",
        "1.png",
        "2.png",
        "3.png",
        "4.png",
        "5.png",
        "6.png",
        "7.png",
        "8.png",
        "9.png",
        "10.png",
    ]

    THEMES: List[Theme] = []

    def __init__(self) -> None:
        self.theme_id: Union[int, None] = None
        self.theme_name: Union[str, None] = None
        self.secret_word: str = ""
        self.guess_word: List[str] = []
        self.guessed_letters: Set[str] = set()
        self.guesses_left: int = 10
        self.win: Union[bool, None] = None

    def get_game_data(self) -> Dict[str, Any]:
        return {
            "theme_id": self.theme_id,
            "theme_name": self.theme_name,
            "secret_word": self.secret_word,
            "guess_word": self.guess_word,
            "guessed_letters": list(self.guessed_letters),
            "guesses_left": self.guesses_left,
            "win": self.win,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HangmanGame':
        game = cls()
        game.theme_id = data["theme_id"]
        game.theme_name = data["theme_name"]
        game.secret_word = data["secret_word"]
        game.guess_word = data["guess_word"]
        game.guessed_letters = set(data["guessed_letters"])
        game.guesses_left = data["guesses_left"]
        game.win = data["win"]
        return game

    @classmethod
    def get_available_themes(cls, db_session: Any) -> List[Theme]:
        themes = db_session.query(Theme).filter_by(activate=True).all()
        cls.THEMES = themes
        return themes

    def get_theme_words(self) -> List[Word]:
        words = db.session.query(Word).filter_by(theme_id=self.theme_id).all()
        return words

    def select_theme(self, theme_id: int) -> None:
        selected_theme = next(
            (theme for theme in self.THEMES if theme.id == theme_id), None
        )
        if selected_theme:
            self.theme_id = theme_id
            self.theme_name = selected_theme.name
        else:
            logger.warning("Invalid theme selected.")
            raise ValueError("Invalid theme selected.")

    def start_single_player_game(self) -> None:
        if self.theme_id is None:
            logger.warning("Theme not selected.")
            raise ValueError("Theme not selected.")
        words = self.get_theme_words()
        self.secret_word = random.choice([word.name for word in words]).lower()
        self.guess_word = ["_" if c.isalpha() else c for c in self.secret_word]
        self.guessed_letters = set()
        self.guesses_left = 10

    def guess_letter(self, letter: str) -> Tuple[str, int]:
        letter = letter.lower()

        if letter in self.guessed_letters:
            return (
                f"You already guessed the letter '{letter}'. Try another letter.",
                404,
            )
        else:
            self.guessed_letters.add(letter)

        if letter in self.secret_word:
            for number_char, char in enumerate(self.secret_word):
                if char == letter:
                    self.guess_word[number_char] = letter

            if "_" not in self.guess_word:
                self.win = True
                return "Congratulations! You guessed the word correctly.", 200

            return f"Good guess!", 201
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                self.win = False
                return f"Game Over. The word was '{self.secret_word}'. Try again!", 202
            return f"Wrong guess. {self.guesses_left} guesses left.", 203

    def get_guesses_left(self) -> int:
        return self.guesses_left

    def get_guessed_letters(self) -> str:
        return ", ".join(self.guessed_letters)

    def is_game_over(self) -> bool:
        return self.get_guesses_left() == 0 or "_" not in self.guess_word

    def get_hangman_drawing(self) -> str:
        if self.guesses_left == 0:
            return self.HANGMAN_DRAWINGS[10]
        stage = 10 - self.guesses_left
        return self.HANGMAN_DRAWINGS[stage]
